# Generated by Django 5.0.11 on 2025-02-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0002_alter_featuredproject_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="featuredproject",
            name="repository_link",
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name="quickproject",
            name="repository_link",
            field=models.URLField(blank=True),
        ),
    ]
