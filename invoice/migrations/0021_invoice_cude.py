# Generated by Django 3.2.8 on 2024-03-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0020_auto_20240316_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='cude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]