# Generated by Django 3.2.8 on 2023-12-18 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0043_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='aiRMKaO9OD', max_length=10),
        ),
    ]
