# Generated by Django 3.2.8 on 2023-12-29 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0007_operation_value_coin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='value_coin',
        ),
    ]