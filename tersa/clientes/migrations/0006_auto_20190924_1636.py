# Generated by Django 2.2.5 on 2019-09-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0005_auto_20190924_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cedula_nit',
            field=models.BigIntegerField(),
        ),
    ]
