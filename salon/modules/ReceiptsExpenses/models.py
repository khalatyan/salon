from django.db import models
from Products.models import Types, Brands
from django.contrib.auth.models import User

class ReceiveProducts(models.Model):
    brand = models.ForeignKey(
            Brands,
            verbose_name = 'Бренд',
            on_delete=models.PROTECT,
    )

    product_type = models.ForeignKey(
        Types,
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )

    number = models.IntegerField(
        verbose_name="Номер продукта"
    )

    date = models.DateField(
            verbose_name='Дата',
    )

    quantity = models.IntegerField(
            verbose_name='Количество',
    )
    volume = models.FloatField(
            verbose_name='Объем',
    )

    def __str__(self):
        return f'{self.product_type} {self.number} {self.date}'

    class Meta:
        verbose_name = "Полученный товар"
        verbose_name_plural = "Полученные товары"


def get_sentinel_user():
    return User.objects.get_or_create(username='Удаленный пользователь')[0]


class SpentProducts(models.Model):

    brand = models.ForeignKey(
        Brands,
        verbose_name='Бренд',
        on_delete=models.PROTECT,
    )

    product_type = models.ForeignKey(
            Types,
            verbose_name = 'Продукт',
            on_delete = models.PROTECT,
    )

    number = models.IntegerField(
            verbose_name = "Номер продукта"
    )

    date = models.DateField(
            verbose_name='Дата',
    )

    volume = models.FloatField(
            verbose_name='Объем',
    )

    user = models.ForeignKey(
            User,
            verbose_name='Пользователь',
            on_delete=models.SET(get_sentinel_user),
    )
    def __str__(self):
        return f'{self.product_type} {self.number} {self.date}'


    class Meta:
        verbose_name = "Потраченный товар"
        verbose_name_plural = "Потраченные товары"


