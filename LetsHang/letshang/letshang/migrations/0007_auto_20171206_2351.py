# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letshang', '0006_userprofile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(default=b'photos/profile-42914_960_720.png', upload_to=b'photos'),
        ),
    ]
