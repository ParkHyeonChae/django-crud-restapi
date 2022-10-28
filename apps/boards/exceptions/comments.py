class RequiredCommentContentError(Exception):
    """required post content error"""

    def __str__(self):
        return "Required Comment Content."


class NotFoundCommentError(Exception):
    """not found comment error"""

    def __str__(self):
        return "Not Found Comment."


class PermissionDeniedUpdateCommentError(Exception):
    """permission denied update comment error"""

    def __str__(self):
        return "Permission Denied Update Comment."


class PermissionDeniedDeleteCommentError(Exception):
    """permission denied delete comment error"""

    def __str__(self):
        return "Permission Denied Delete Comment."
