# Generated by Django 4.1.2 on 2022-12-01 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200, null=True)),
                ("phone", models.CharField(max_length=200, null=True)),
                ("email", models.CharField(max_length=200, null=True)),
                ("skill", models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Job",
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
                ("job_name", models.CharField(max_length=200, null=True)),
                ("pay", models.FloatField(null=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Video", "Video"),
                            ("Native", "Native"),
                            ("Mobile", "Mobile"),
                            ("Display", "Display"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "job_description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("date_added", models.DateTimeField(auto_now_add=True, null=True)),
                ("job_id", models.IntegerField(max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("date", models.DateTimeField(auto_now_add=True, null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Recently Received", "Recently Received"),
                            ("Working", "Working"),
                            ("Awaiting Instructions", "Awaiting Instructions"),
                            ("Finished", "Finished"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.customer",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="app.job",
                    ),
                ),
            ],
        ),
    ]
