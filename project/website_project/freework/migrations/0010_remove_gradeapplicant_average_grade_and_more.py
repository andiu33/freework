# Generated by Django 4.1 on 2022-10-06 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("freework", "0009_alter_gradeapplicant_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="gradeapplicant", name="average_grade",),
        migrations.AddField(
            model_name="applicant",
            name="soft_skills",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="freework.gradeapplicant",
            ),
        ),
    ]
