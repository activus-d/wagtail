# Generated by Django 5.0.1 on 2024-03-15 21:20

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tests", "0034_custompermissionmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="ModelWithCustomManager",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            managers=[
                ("instances", django.db.models.manager.Manager()),
            ],
        ),
    ]
