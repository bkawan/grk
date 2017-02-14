# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-14 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.PositiveIntegerField(default='34', unique=True),
            preserve_default=False,
        ),
    ]