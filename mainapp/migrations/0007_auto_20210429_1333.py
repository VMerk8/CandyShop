# Generated by Django 3.1.6 on 2021-04-29 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210403_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='final_price',
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Общая Цена'),
        ),
    ]
