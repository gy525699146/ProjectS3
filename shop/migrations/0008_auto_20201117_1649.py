# Generated by Django 3.1.3 on 2020-11-17 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20201117_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
