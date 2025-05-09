# Generated by Django 4.2.9 on 2024-01-25 17:46
import django.utils.timezone
import django_extensions.db.fields
from django.db import migrations
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("integrations", "0010_remove_old_jsonfields"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="integration",
            options={"get_latest_by": "modified"},
        ),
        migrations.AddField(
            model_name="integration",
            name="created",
            field=django_extensions.db.fields.CreationDateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="created",
                null=True,
                blank=True,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="integration",
            name="modified",
            field=django_extensions.db.fields.ModificationDateTimeField(
                auto_now=True,
                verbose_name="modified",
                null=True,
                blank=True,
            ),
        ),
    ]
