# Generated by Django 3.2.8 on 2024-01-30 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0080_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='h29PPXqwQs', max_length=10),
        ),
    ]