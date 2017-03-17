# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-16 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0033_auto_20170316_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='plan',
            field=models.CharField(blank=True, choices=[('family_monthly', 'Family Monthly Subscription'), ('family_yearly', 'Family Yearly Subscription'), ('team_monthly', 'Team Monthly Subscription'), ('team_yearly', 'Team Yearly Subscription'), ('basic_monthly', 'Basic Monthly Subscription'), ('basic_yearly', 'Basic Yearly Subscription')], max_length=100),
        ),
        migrations.AlterField(
            model_name='historicalbook',
            name='plan',
            field=models.CharField(blank=True, choices=[('family_monthly', 'Family Monthly Subscription'), ('family_yearly', 'Family Yearly Subscription'), ('team_monthly', 'Team Monthly Subscription'), ('team_yearly', 'Team Yearly Subscription'), ('basic_monthly', 'Basic Monthly Subscription'), ('basic_yearly', 'Basic Yearly Subscription')], max_length=100),
        ),
    ]
