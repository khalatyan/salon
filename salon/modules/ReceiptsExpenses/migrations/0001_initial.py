# Generated by Django 3.0.8 on 2020-07-31 19:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SpentProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер продукта')),
                ('date', models.DateField(verbose_name='Дата')),
                ('volume', models.FloatField(verbose_name='Объем')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.Brands', verbose_name='Бренд')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.Types', verbose_name='Продукт')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Потраченный товар',
                'verbose_name_plural': 'Потраченные товары',
            },
        ),
        migrations.CreateModel(
            name='ReceiveProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер продукта')),
                ('date', models.DateField(verbose_name='Дата')),
                ('quantity', models.IntegerField(verbose_name='Количество')),
                ('volume', models.FloatField(verbose_name='Объем')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.Brands', verbose_name='Бренд')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.Types', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Полученный товар',
                'verbose_name_plural': 'Полученные товары',
            },
        ),
    ]
