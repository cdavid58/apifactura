# Generated by Django 3.2.8 on 2024-02-09 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0082_alter_branch_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='psswd',
            field=models.CharField(default='yuzwj09opf', max_length=10),
        ),
    ]
