# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-04 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_category_local_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='local_img',
            field=models.ImageField(default='null', upload_to='local_img'),
        ),
    ]
