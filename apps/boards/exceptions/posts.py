class RequiredPostTitleError(Exception):
    """required post title error"""

    def __str__(self):
        return "Required Post Title."


class RequiredPostContentError(Exception):
    """required post content error"""

    def __str__(self):
        return "Required Post Content."


class NotFoundPostError(Exception):
    """not found post error"""

    def __str__(self):
        return "Not Found Post."


class PermissionDeniedUpdatePostError(Exception):
    """permission denied update post error"""

    def __str__(self):
        return "Permission Denied Update Post."


class PermissionDeniedDeletePostError(Exception):
    """permission denied delete post error"""

    def __str__(self):
        return "Permission Denied Delete Post."
