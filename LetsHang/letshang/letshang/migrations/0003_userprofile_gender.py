# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letshang', '0002_userprofile_most_recent_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default='not determined', max_length=20),
            preserve_default=False,
        ),
    ]