# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-25 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='fileClassify',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='share.FileClassify'),
        ),
        migrations.AlterField(
            model_name='file',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.User'),
        ),
    ]
