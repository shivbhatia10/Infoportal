# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-08 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infoportal', '0004_auto_20171208_0923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='catagory',
            new_name='category',
        ),
    ]
