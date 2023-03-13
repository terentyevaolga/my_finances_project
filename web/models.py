from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MoneySlotTag(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title


class MoneySlot(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    amount_spent = models.IntegerField(verbose_name='Потраченная сумма')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    tags = models.ManyToManyField(MoneySlotTag)
    image = models.ImageField(upload_to='money_slots/', null=True, blank=True, verbose_name='Изображение')

