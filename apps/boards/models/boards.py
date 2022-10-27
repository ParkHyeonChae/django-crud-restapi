from django.db import models


class Board(models.Model):
    """board model"""

    name = models.CharField(max_length=255)
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "board"
        verbose_name_plural = "Board (게시판)"
