# Generated by Django 3.0.11 on 2021-01-17 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Election",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=1000)),
                ("enable_multiple_submissions", models.BooleanField(default=False)),
                ("election_email_domain", models.CharField(max_length=100)),
                ("submission_start_time", models.DateTimeField(blank=True, null=True)),
                ("submission_end_time", models.DateTimeField(blank=True, null=True)),
                ("voting_start_time", models.DateTimeField(blank=True, null=True)),
                ("voting_end_time", models.DateTimeField(blank=True, null=True)),
                (
                    "manager",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="elections",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Position",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=2000)),
                (
                    "election",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="positions",
                        to="elections.Election",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("platform", models.CharField(max_length=2000)),
                (
                    "position",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="candidates",
                        to="elections.Position",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="candidacies",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
