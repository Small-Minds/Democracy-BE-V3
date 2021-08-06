# Generated by Django 3.0.11 on 2021-03-12 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("elections", "0008_vote_vote_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vote",
            name="candidate",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="votes",
                to="elections.Candidate",
            ),
        ),
    ]