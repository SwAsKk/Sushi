# Generated by Django 4.0.3 on 2022-05-29 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_classicset_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.IntegerField(verbose_name='Цена маленькая пицца'),
        ),
    ]
