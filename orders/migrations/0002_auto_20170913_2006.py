# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 09:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productinorder',
            options={'verbose_name': 'Tovar v zakaze', 'verbose_name_plural': 'Tovary v zakaze'},
        ),
    ]
