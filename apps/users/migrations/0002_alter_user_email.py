# Generated by Django 4.1.2 on 2022-10-27 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
    ]