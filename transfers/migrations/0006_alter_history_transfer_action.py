# Generated by Django 3.2.8 on 2024-01-12 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfers', '0005_auto_20240110_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history_transfer',
            name='action',
            field=models.CharField(choices=[('Entrance', 'Entrance'), ('Exit', 'Exit'), ('Returned', 'Returned')], max_length=10),
        ),
    ]