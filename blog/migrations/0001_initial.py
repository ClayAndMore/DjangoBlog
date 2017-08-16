# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('content', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'message',
            },
        ),
    ]
