# Generated by Django 2.1.2 on 2018-12-01 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181201_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity_stocked',
            field=models.IntegerField(default=0),
        ),
    ]
