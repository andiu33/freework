# Generated by Django 4.1 on 2022-09-30 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("freework", "0007_applicant_profile_recruiter_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant",
            name="interest",
            field=models.CharField(
                choices=[
                    ("Humanidades", "Humanidades"),
                    ("Ciencias exactas", "Ciencias exactas"),
                    ("Ciencias naturales", "Ciencias naturales"),
                    ("Ciencias sociales", "Ciencias sociales"),
                    ("Ciencias de la salud", "Ciencias de la salud"),
                    ("Negocios", "Negocios"),
                    ("Leyes", "Leyes"),
                    ("Tecnología", "Tecnologia"),
                ],
                default="1",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="applicant",
            name="phone",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="profile",
            field=models.CharField(
                choices=[("Aspirante", "Aspirante"), ("Reclutador", "Reclutador")],
                default="1",
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="recruiter",
            name="phone",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="GradeApplicant",
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
                ("first_name", models.CharField(max_length=255, null=True)),
                ("last_name", models.CharField(max_length=255, null=True)),
                ("relation", models.CharField(max_length=255, null=True)),
                ("soft_skills", models.PositiveIntegerField(blank=True, null=True)),
                ("hard_skills", models.PositiveIntegerField(blank=True, null=True)),
                ("average_grade", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]