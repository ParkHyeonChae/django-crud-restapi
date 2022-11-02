"""
board app api exception data
"""

HTTP_401_NOT_AUTHENTICATED = {
    "code": "NOT_AUTHENTICATED",
    "detail": "로그인이 필요합니다.",
}
HTTP_400_INVALID_POST_BODY = {
    "code": "INVALID_POST_BODY",
    "detail": "게시글 작성에 필요한 항목들이 유효하지 않습니다.",
}
HTTP_404_NOT_FOUND_POST = {
    "code": "NOT_FOUND_POST",
    "detail": "게시글을 찾을 수 없습니다.",
}
HTTP_403_PERMISSION_DENIED_UPDATE_POST = {
    "code": "PERMISSION_DENIED_UPDATE_POST",
    "detail": "게시글을 수정할 권한이 없습니다.",
}
HTTP_403_PERMISSION_DENIED_DELETE_POST = {
    "code": "PERMISSION_DENIED_DELETE_POST",
    "detail": "게시글을 삭제할 권한이 없습니다.",
}
HTTP_400_INVALID_COMMENT_BODY = {
    "code": "INVALID_COMMENT_BODY",
    "detail": "댓글 작성에 필요한 항목들이 유효하지 않습니다.",
}
HTTP_404_NOT_FOUND_COMMENT = {
    "code": "NOT_FOUND_COMMENT",
    "detail": "댓글을 찾을 수 없습니다.",
}
HTTP_403_PERMISSION_DENIED_UPDATE_COMMENT = {
    "code": "PERMISSION_DENIED_UPDATE_COMMENT",
    "detail": "댓글을 수정할 권한이 없습니다.",
}
HTTP_403_PERMISSION_DENIED_DELETE_COMMENT = {
    "code": "PERMISSION_DENIED_DELETE_COMMENT",
    "detail": "댓글을 삭제할 권한이 없습니다.",
}
