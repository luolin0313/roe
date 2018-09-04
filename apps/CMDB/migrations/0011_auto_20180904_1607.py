# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-04 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMDB', '0010_auto_20180904_1550'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='service_assets',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='service_assets',
            name='project',
        ),
        migrations.DeleteModel(
            name='Project_Assets',
        ),
        migrations.DeleteModel(
            name='Service_Assets',
        ),
    ]
