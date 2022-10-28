"""
Board APP API Exception Data
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
