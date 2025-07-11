# Generated by Django 5.0.11 on 2025-01-27 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Certificate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=60)),
                ("institution_name", models.CharField(max_length=60)),
                ("date_earned", models.DateField(auto_now=True)),
                ("certificate_file", models.FileField(upload_to="uploads/")),
            ],
        ),
    ]
