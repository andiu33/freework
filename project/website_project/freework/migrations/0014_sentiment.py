# Generated by Django 4.1 on 2022-10-16 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("freework", "0013_gradeapplicant_comment_gradeapplicant_comment_sr"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sentiment",
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
                ("text_to_analyze", models.CharField(max_length=255)),
                ("text_analyzed", models.CharField(max_length=255)),
            ],
        ),
    ]