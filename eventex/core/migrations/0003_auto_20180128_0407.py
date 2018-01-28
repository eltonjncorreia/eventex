# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-28 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_talk_speakers'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='contact',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='talk',
            name='speakers',
            field=models.ManyToManyField(blank=True, to='core.Speaker', verbose_name='palestrantes'),
        ),
    ]