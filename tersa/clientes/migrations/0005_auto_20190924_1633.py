# Generated by Django 2.2.5 on 2019-09-24 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_auto_20190924_1632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='numero_celular',
            new_name='telefono',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='numero_telefono',
        ),
    ]
