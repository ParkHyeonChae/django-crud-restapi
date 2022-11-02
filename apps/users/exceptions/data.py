"""
user app api exception data
"""

HTTP_401_AUTHENTICATION_FAILED = {
    "code": "AUTHENTICATION_FAILED",
    "detail": "로그인 정보가 일치하지 않습니다.",
}
HTTP_400_INVALID_USER_SIGNIN_BODY = {
    "code": "INVALID_USER_SIGNIN_BODY",
    "detail": "로그인에 필요한 필수 항목을 입력해주세요.",
}
HTTP_400_IS_DORMANT_USER = {
    "code": "IS_DORMANT_USER",
    "detail": "휴면처리된 사용자입니다.",
}
HTTP_400_INVALID_USER_SIGNUP_BODY = {
    "code": "INVALID_USER_SIGNUP_BODY",
    "detail": "회원가입에 필요한 필수 항목을 입력해주세요.",
}
HTTP_400_IS_ALREADY_EXIST_USER_EMAIL = {
    "code": "IS_ALREADY_EXIST_USER_EMAIL",
    "detail": "이미 존재하는 이메일입니다.",
}
