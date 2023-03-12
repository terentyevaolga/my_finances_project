from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MoneySlotTag(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class MoneySlot(models.Model):
    title = models.CharField(max_length=256)
    amount_spent = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(MoneySlotTag)
