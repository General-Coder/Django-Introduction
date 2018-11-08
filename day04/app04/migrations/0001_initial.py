# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-25 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='语言名字')),
                ('desc', models.CharField(max_length=100, verbose_name='描述')),
            ],
        ),
    ]