# Generated by Django 4.0.3 on 2022-05-29 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_pizza_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='priceL',
            field=models.IntegerField(default=100, verbose_name='Цена большой пиццы'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='priceM',
            field=models.IntegerField(default=100, verbose_name='Цена средней пиццы'),
        ),
        migrations.AddField(
            model_name='pizza',
            name='priceS',
            field=models.IntegerField(default=100, verbose_name='Цена маленькой пиццы'),
        ),
    ]
