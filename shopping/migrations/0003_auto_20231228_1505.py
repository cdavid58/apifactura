# Generated by Django 3.2.8 on 2023-12-28 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0002_history_shopping'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='annulled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shopping',
            name='cancelled',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Pass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_pass', models.IntegerField()),
                ('amount', models.FloatField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('shopping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.shopping')),
            ],
        ),
    ]