# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 17:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=8, lowercase=True, unique=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='')),
                ('tagline', models.CharField(blank=True, max_length=150)),
                ('bio', models.TextField(blank=True, max_length=2000)),
                ('location', models.CharField(blank=True, max_length=5)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='social', to='core.UserProfile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]