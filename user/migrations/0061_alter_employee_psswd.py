# Generated by Django 3.2.8 on 2024-01-02 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0060_alter_employee_psswd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='psswd',
            field=models.CharField(default='FZ9Mkf2VPddXXAO74t6T', max_length=20, unique=True),
        ),
    ]