# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-16 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bankaccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(verbose_name=5)),
                ('balance', models.IntegerField(verbose_name=10)),
                ('tax', models.IntegerField(verbose_name=10)),
            ],
        ),
    ]