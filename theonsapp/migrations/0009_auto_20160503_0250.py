# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theonsapp', '0008_auto_20160503_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(blank=True, default='No Description', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.CharField(blank=True, default='No Description', max_length=255, null=True),
        ),
    ]
