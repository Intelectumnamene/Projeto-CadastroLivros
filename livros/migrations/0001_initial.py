# Generated by Django 4.2.7 on 2023-11-16 01:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Meus_livros",
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
                ("meus_livros", models.TextField(max_length=255)),
                ("valor", models.FloatField()),
                ("pago", models.BooleanField(default=False)),
                ("data", models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
