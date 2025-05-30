# Generated by Django 4.2.17 on 2025-01-29 15:02

import django.db.models.deletion
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.always()

    dependencies = [
        ("builds", "0059_add_version_date_index"),
        ("projects", "0143_addons_flyout_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addonsconfig",
            name="options_base_version",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="builds.version",
                verbose_name="Base version to compare against (eg. DocDiff, File Tree Diff)",
            ),
        ),
    ]
