# Generated by Django 3.2.8 on 2024-02-26 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0102_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='internal_email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='fRKOJUpR9V8Tge3e9EoW', max_length=20, unique=True),
        ),
    ]
