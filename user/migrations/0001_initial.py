# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('profile_image', models.URLField(default='', blank=True)),
                ('gender', models.CharField(default='', max_length=20, blank=True)),
                ('country', models.CharField(default='', max_length=50, blank=True)),
                ('city', models.CharField(default='', max_length=200, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('about', models.CharField(default='', max_length=100, blank=True)),
                ('achievements', models.TextField(default='{}')),
                ('followers', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('following', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
