# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-17 03:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100)),
                ('website', models.URLField(verbose_name='Website')),
                ('photo', models.URLField(verbose_name='Photo')),
                ('description', models.TextField(verbose_name='Descrição')),
            ],
        ),
    ]