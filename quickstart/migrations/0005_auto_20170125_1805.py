# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_auto_20170125_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderhasproducts',
            name='orderId',
        ),
        migrations.RemoveField(
            model_name='orderhasproducts',
            name='productId',
        ),
        migrations.AddField(
            model_name='orderhasproducts',
            name='order',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='quickstart.BangOrder'),
        ),
        migrations.AddField(
            model_name='orderhasproducts',
            name='product',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='quickstart.Product'),
        ),
    ]
