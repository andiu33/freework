# Generated by Django 4.1 on 2022-10-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("freework", "0015_sentiment_analyze_save"),
    ]

    operations = [
        migrations.RemoveField(model_name="sentiment", name="text_analyzed",),
        migrations.AlterField(
            model_name="sentiment",
            name="analyze_save",
            field=models.CharField(max_length=255),
        ),
    ]
