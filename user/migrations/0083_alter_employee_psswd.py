# Generated by Django 3.2.8 on 2024-02-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0082_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='HMDAffr6w3wyn3qYKpug', max_length=20, unique=True),
        ),
    ]