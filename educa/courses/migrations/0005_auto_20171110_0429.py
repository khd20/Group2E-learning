# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-10 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-created',)},
        ),
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=models.TextField(),
        ),
    ]
