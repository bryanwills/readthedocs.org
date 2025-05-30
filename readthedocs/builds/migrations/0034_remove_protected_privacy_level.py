# Generated by Django 2.2.20 on 2021-04-29 18:49
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("builds", "0033_dont_cascade_delete_builds"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="privacy_level",
            field=models.CharField(
                choices=[("public", "Public"), ("private", "Private")],
                default="public",
                help_text="Level of privacy for this Version.",
                max_length=20,
                verbose_name="Privacy Level",
            ),
        ),
    ]
