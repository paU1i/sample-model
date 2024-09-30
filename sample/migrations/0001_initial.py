# Generated by Django 5.1.1 on 2024-09-24 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "andrew_id",
                    models.CharField(max_length=8, primary_key=True, serialize=False),
                ),
                ("fname", models.CharField(max_length=8)),
                ("lname", models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=200)),
                ("number", models.CharField(max_length=6)),
                ("students", models.ManyToManyField(to="sample.student")),
            ],
        ),
    ]
