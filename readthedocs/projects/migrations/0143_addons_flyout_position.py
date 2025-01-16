# Generated by Django 4.2.17 on 2025-01-08 11:15

from django.db import migrations, models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.before_deploy

    dependencies = [
        ('projects', '0142_update_dj_simple_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addonsconfig',
            name='flyout_enabled',
            field=models.BooleanField(default=True, verbose_name='Enabled'),
        ),
        migrations.AddField(
            model_name='addonsconfig',
            name='flyout_position',
            field=models.CharField(blank=True, choices=[(None, 'Default (from theme or Read the Docs)'), ('bottom-left', 'Bottom left'), ('bottom-right', 'Bottom right'), ('top-left', 'Top left'), ('top-right', 'Top right')], default=None, max_length=64, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='historicaladdonsconfig',
            name='flyout_enabled',
            field=models.BooleanField(default=True, verbose_name='Enabled'),
        ),
        migrations.AddField(
            model_name='historicaladdonsconfig',
            name='flyout_position',
            field=models.CharField(blank=True, choices=[(None, 'Default (from theme or Read the Docs)'), ('bottom-left', 'Bottom left'), ('bottom-right', 'Bottom right'), ('top-left', 'Top left'), ('top-right', 'Top right')], default=None, max_length=64, null=True, verbose_name='Position'),
        ),
    ]