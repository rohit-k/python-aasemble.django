# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-14 09:26
from __future__ import unicode_literals

from django.db import migrations, models

from aasemble.utils import run_cmd


def import_key_data(apps, schema_editor):
    Repository = apps.get_model("buildsvc", "Repository")
    for repo in Repository.objects.all():
        repo.key_data = key_data(repo)
        repo.save()


def key_data(repository):
    if repository.key_id:
        return run_cmd(['gpg', '-a', '--export', repository.key_id])


class Migration(migrations.Migration):

    dependencies = [
        ('buildsvc', '0018_repository_key_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='key_data',
            field=models.TextField(null=False),
        ),
        migrations.RunPython(import_key_data),
    ]
