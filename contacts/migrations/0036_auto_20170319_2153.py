# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-03-19 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0009_auto_20170319_2153'),
        ('contacts', '0035_auto_20170317_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.StripeCustomer'),
        ),
        migrations.AddField(
            model_name='bookowner',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.StripeCustomer'),
        ),
        migrations.AddField(
            model_name='historicalbook',
            name='customer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='payments.StripeCustomer'),
        ),
        migrations.AddField(
            model_name='historicalbookowner',
            name='customer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='payments.StripeCustomer'),
        ),
    ]
