# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=250, unique=True),
            preserve_default=False,
        ),
    ]
