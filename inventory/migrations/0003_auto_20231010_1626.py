# Generated by Django 3.2.8 on 2023-10-10 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20231010_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]