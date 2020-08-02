from django.db import models
from django.contrib import admin

class Types(models.Model):
    name = models.CharField(
        verbose_name='Тип продукта',
        max_length=50
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы продуктов"


class Brands(models.Model):
    name = models.CharField(
        verbose_name='Бренд продукта',
        max_length=50
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды продуктов"

class Products(models.Model):
    product_type = models.ForeignKey(
        Types,
        verbose_name='Продукт',
        on_delete=models.PROTECT,
    )

    number = models.CharField(
        null=True,
        blank=True,
        max_length = 20,
        verbose_name="Номер продукта"
    )

    volume_sp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Потратили"
    )

    volume_rp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Получили"
    )

    volume = models.FloatField(
        verbose_name="Осталось"
    )


    def __str__(self):
        return f'{self.product_type} {self.number}'

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

