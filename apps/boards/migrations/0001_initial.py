# Generated by Django 4.1.2 on 2022-10-27 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Board",
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
                ("name", models.CharField(max_length=255)),
                ("is_published", models.BooleanField(default=True)),
                ("updated_at", models.DateTimeField(null=True)),
                ("created_at", models.DateTimeField()),
            ],
            options={
                "verbose_name_plural": "Board (게시판)",
                "db_table": "board",
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField(max_length=1000)),
                ("view_count", models.PositiveIntegerField(default=0)),
                ("deleted_at", models.DateTimeField(null=True)),
                ("updated_at", models.DateTimeField(null=True)),
                ("created_at", models.DateTimeField()),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="boards.board"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Post (게시글)",
                "db_table": "post",
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("content", models.TextField(max_length=1000)),
                ("deleted_at", models.DateTimeField(null=True)),
                ("updated_at", models.DateTimeField(null=True)),
                ("created_at", models.DateTimeField()),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="boards.post"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Comment (댓글)",
                "db_table": "comment",
            },
        ),
    ]
