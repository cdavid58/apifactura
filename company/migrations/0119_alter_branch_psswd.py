# Generated by Django 3.2.8 on 2024-05-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0118_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='43FjTPqanG', max_length=10),
        ),
    ]
