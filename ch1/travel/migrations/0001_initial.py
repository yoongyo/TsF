# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-04 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('visited_country', models.CharField(max_length=20)),
                ('interest', models.CharField(max_length=20)),
                ('content', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.Category')),
            ],
        ),
    ]