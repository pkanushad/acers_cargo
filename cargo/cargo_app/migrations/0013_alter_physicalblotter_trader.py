# Generated by Django 4.1.2 on 2022-11-04 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0012_bookmodel_counterpartymodel_holidaymodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicalblotter',
            name='Trader',
            field=models.ForeignKey(default='Select', on_delete=django.db.models.deletion.CASCADE, to='cargo_app.tradermodel'),
        ),
    ]
