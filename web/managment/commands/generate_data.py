from django.core.management.base import BaseCommand

# manage,py не видит этот класс(


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(123)


        # user = User.objects.first()
        # tags = MoneySlotTag.objects.filter(user=user)
        #
        # money_slots = []
        #
        # for day_index in range(30):
        #
        #     for slot_index in range(random.randint(5, 10)):
        #
        #         money_slots.append(MoneySlot(
        #             title=f'generated {day_index}-{slot_index}',
        #             amount_spent=random.randint(1, 10000),
        #             user=user
        #         ))
        #
        # saved_money_slots = MoneySlot.objects.bulk_create(money_slots)
        # money_slot_tags = []
        # for money_slot in saved_money_slots:
        #     count_of_tags = random.randint(0, len(tags))
        #     for tag_index in range(count_of_tags):
        #         money_slot_tags.append(
        #             MoneySlot.tags.through(moneyslot_id=money_slot.id, moneyslottag_id=tags[tag_index].id)
        #         )
        # MoneySlot.tags.through.objects.bulk_create(money_slot_tags)