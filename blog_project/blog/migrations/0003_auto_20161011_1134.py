# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-11 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161011_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment', verbose_name=b'\xe7\x88\xb6\xe7\xba\xa7\xe8\xaf\x84\xe8\xae\xba'),
        ),
    ]