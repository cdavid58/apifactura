# Generated by Django 3.2.8 on 2024-05-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0114_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='rp7KG2xaT3XAXxvlonBq', max_length=20, unique=True),
        ),
    ]