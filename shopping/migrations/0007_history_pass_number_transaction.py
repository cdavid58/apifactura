# Generated by Django 3.2.8 on 2024-02-20 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_history_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='history_pass',
            name='number_transaction',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]