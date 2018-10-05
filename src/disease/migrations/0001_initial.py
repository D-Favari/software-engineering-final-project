# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-09-30 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=120)),
                ('count', models.IntegerField(null=True)),
            ],
        ),
    ]