# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('nick_name', models.CharField(max_length=16)),
                ('mobile_no', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=1)),
                ('create_time', models.DateTimeField(verbose_name='create time')),
            ],
        ),
    ]