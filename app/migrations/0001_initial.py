# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 02:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ModelA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ModelB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('related_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ModelA')),
            ],
        ),
        migrations.CreateModel(
            name='ModelC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('related_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ModelA')),
            ],
        ),
        migrations.AddField(
            model_name='mainmodel',
            name='model_a',
            field=models.ManyToManyField(to='app.ModelA'),
        ),
        migrations.AddField(
            model_name='mainmodel',
            name='model_b',
            field=models.ManyToManyField(to='app.ModelB'),
        ),
        migrations.AddField(
            model_name='mainmodel',
            name='model_c',
            field=models.ManyToManyField(to='app.ModelC'),
        ),
    ]