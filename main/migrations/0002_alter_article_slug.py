# Generated by Django 3.2 on 2022-03-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="slug",
            field=models.SlugField(unique=True, verbose_name="slug"),
        ),
    ]
