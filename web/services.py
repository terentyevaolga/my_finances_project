import csv


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



