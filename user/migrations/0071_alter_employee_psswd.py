# Generated by Django 3.2.8 on 2024-01-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0070_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='UEE7CKTUVrSPLvBkjR0E', max_length=20, unique=True),
        ),
    ]