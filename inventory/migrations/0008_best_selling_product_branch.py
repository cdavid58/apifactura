# Generated by Django 3.2.8 on 2024-01-30 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0081_alter_branch_psswd'),
        ('inventory', '0007_best_selling_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='best_selling_product',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.branch'),
        ),
    ]