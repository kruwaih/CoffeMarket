# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0006_auto_20170821_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='apartment_Number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='extra_instruction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='floor',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
