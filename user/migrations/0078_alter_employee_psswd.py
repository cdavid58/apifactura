# Generated by Django 3.2.8 on 2024-02-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0077_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='qSopJueKTHWUoF2ODk5z', max_length=20, unique=True),
        ),
    ]