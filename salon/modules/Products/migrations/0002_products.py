# Generated by Django 3.0.8 on 2020-08-01 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер продукта')),
                ('volume_sp', models.FloatField(verbose_name='Потратили')),
                ('volume_rp', models.FloatField(verbose_name='Получили')),
                ('volume', models.FloatField(verbose_name='Осталось')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Products.Types', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды продуктов',
            },
        ),
    ]