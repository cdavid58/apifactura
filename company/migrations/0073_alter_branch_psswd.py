# Generated by Django 3.2.8 on 2024-01-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0072_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='svHj7n51L6', max_length=10),
        ),
    ]