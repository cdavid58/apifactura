# Generated by Django 3.2.8 on 2024-01-02 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emails', '0002_auto_20240102_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='time_register',
        ),
        migrations.AlterField(
            model_name='emails',
            name='date_register',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]