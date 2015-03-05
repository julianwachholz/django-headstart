# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('email', models.EmailField(unique=True, max_length=75, verbose_name='email')),
                ('is_active', models.BooleanField(verbose_name='active', default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(verbose_name='groups', blank=True, related_query_name='user', related_name='user_set', to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', blank=True, related_query_name='user', related_name='user_set', to='auth.Permission', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name': 'user',
                'ordering': ['email'],
                'verbose_name_plural': 'users',
            },
            bases=(models.Model,),
        ),
    ]
