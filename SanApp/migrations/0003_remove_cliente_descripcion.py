# Generated by Django 4.1.4 on 2023-01-25 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SanApp', '0002_cliente_descripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='descripcion',
        ),
    ]
