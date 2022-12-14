# Generated by Django 4.1 on 2022-10-16 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("freework", "0017_rename_comment_gradeapplicant_comment_save_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="gradeapplicant",
            name="sentiment",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="freework.sentiment",
            ),
        ),
        migrations.AlterField(
            model_name="gradeapplicant",
            name="comment_save",
            field=models.CharField(default="1", max_length=255),
        ),
        migrations.AlterField(
            model_name="gradeapplicant",
            name="comment_to_analyze",
            field=models.CharField(default="1", max_length=255),
        ),
    ]
