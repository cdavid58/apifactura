# Generated by Django 3.2.8 on 2024-02-20 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0084_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='dokX5zNSbU2EO8CqL12L', max_length=20, unique=True),
        ),
    ]