# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adventure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('required', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('earned', models.DateField(null=True)),
                ('reported', models.DateField(null=True)),
                ('purchased', models.DateField(null=True)),
                ('delivered', models.DateField(null=True)),
                ('adventure', models.ForeignKey(to='awards.Adventure')),
            ],
        ),
        migrations.CreateModel(
            name='Den',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Scout',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(unique=True, max_length=64)),
                ('awards', models.ManyToManyField(to='awards.Adventure', through='awards.Award')),
                ('den', models.ForeignKey(to='awards.Den')),
            ],
        ),
        migrations.AddField(
            model_name='award',
            name='scout',
            field=models.ForeignKey(to='awards.Scout'),
        ),
        migrations.AddField(
            model_name='adventure',
            name='den',
            field=models.ForeignKey(to='awards.Den'),
        ),
    ]
