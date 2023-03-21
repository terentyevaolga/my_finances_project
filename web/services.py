import csv

from web.models import MoneySlot, MoneySlotTag


def filter_moneyslots(moneyslots_qs, filters: dict):
    if filters['search']:
        moneyslots_qs = moneyslots_qs.filter(title__icontains=filters['search'])

    if filters['amount_spent']:
        moneyslots_qs = moneyslots_qs.filter(amount_spent=filters['amount_spent'])
    return moneyslots_qs


def export_moneyslots_csv(moneyslots_qs, response):
    writer = csv.writer(response)
    writer.writerow(('title', 'amount_spent', 'tags'))

    for moneyslot in moneyslots_qs:
        writer.writerow((moneyslot.title, moneyslot.amount_spent,
                         " ".join([t.title for t in moneyslot.tags.all()])
                         ))

    return response


def import_moneyslots_from_csv(file, user_id):
    strs_from_file = (row.decode() for row in file)
    reader = csv.DictReader(strs_from_file)

    moneyslots = []
    moneyslot_tags = []
    for row in reader:
        moneyslots.append(MoneySlot(
            title=row['title'],
            amount_spent=row['amount_spent'],
            user_id=user_id
        ))
        moneyslot_tags.append(row['tags'].split(" ") if row['tags'] else [])

    saved_moneyslots = MoneySlot.objects.bulk_create(moneyslots)

    tags_map = dict(MoneySlotTag.objects.all().values_list('title', 'id'))
    money_slot_tags = []
    for moneyslot, moneyslot_tags_item in zip(saved_moneyslots, moneyslot_tags):
        for tag in moneyslot_tags_item:
            tag_id = tags_map[tag]
            money_slot_tags.append(
                MoneySlot.tags.through(moneyslot_id=moneyslot.id, moneyslottag_id=tag_id)
            )
    MoneySlot.tags.through.objects.bulk_create(money_slot_tags)
