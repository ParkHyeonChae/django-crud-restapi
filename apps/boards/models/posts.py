from django.db import models


class Post(models.Model):
    """post model"""

    board = models.ForeignKey("boards.Board", on_delete=models.PROTECT)
    user = models.ForeignKey("users.User", on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    view_count = models.PositiveIntegerField(default=0)
    deleted_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "post"
        verbose_name_plural = "Post (게시글)"
