# Generated by Django 3.2.8 on 2024-02-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0008_alter_history_pass_number_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='pass',
            name='employee',
            field=models.JSONField(blank=True, null=True),
        ),
    ]