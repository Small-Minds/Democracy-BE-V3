# Generated by Django 3.0.11 on 2021-02-24 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("elections", "0003_ballot_vote"),
    ]

    operations = [
        migrations.AddField(
            model_name="election",
            name="subtitle",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
    ]
