# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bangapi', '0009_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderhasproducts',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bangapi.BangOrder'),
        ),
        migrations.AlterField(
            model_name='orderhasproducts',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bangapi.Product'),
        ),
    ]
