# Generated by Django 3.2.8 on 2023-12-28 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0054_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='4nlxrVzotf', max_length=10),
        ),
    ]