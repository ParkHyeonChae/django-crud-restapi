from django.db import models


class Comment(models.Model):
    """comment model"""

    post = models.ForeignKey("boards.Post", on_delete=models.PROTECT)
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)
    content = models.TextField(max_length=1000)
    deleted_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "comment"
        verbose_name_plural = "Comment (댓글)"
