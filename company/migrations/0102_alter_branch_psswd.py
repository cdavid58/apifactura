# Generated by Django 3.2.8 on 2024-02-21 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0101_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='nreoDYy3Gc', max_length=10),
        ),
    ]
