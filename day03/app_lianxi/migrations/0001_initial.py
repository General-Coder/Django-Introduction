# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-10-24 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='家')),
            ],
            options={
                'db_table': 'zd_home',
            },
        ),
        migrations.CreateModel(
            name='Humen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='人名')),
                ('jia', models.OneToOneField(max_length=20, on_delete=django.db.models.deletion.CASCADE, to='app_lianxi.Home', verbose_name='人的家')),
            ],
            options={
                'db_table': 'zd_humen',
            },
        ),
    ]