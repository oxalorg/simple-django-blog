# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 06:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160608_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='html',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
