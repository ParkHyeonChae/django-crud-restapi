from django.utils.encoding import force_str
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.utils.serializer_helpers import ReturnDict, ReturnList


class ErrorDetail(str):
    code = None

    def __new__(cls, code=None, string=None):
        self = super().__new__(cls, string)
        self.code = code
        return self

    def __eq__(self, other):
        r = super().__eq__(other)
        try:
            return r and self.code == other.code
        except AttributeError:
            return r

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "ErrorDetail(string=%r, code=%r)" % (
            str(self),
            self.code,
        )

    def __hash__(self):
        return hash(str(self))


def _get_error_details(code, detail):
    if isinstance(detail, list):
        ret = [_get_error_details(code, item) for item in detail]
        if isinstance(detail, ReturnList):
            return ReturnList(ret, serializer=detail.serializer)
        return ret
    elif isinstance(detail, dict):
        ret = {key: _get_error_details(value, code) for key, value in detail.items()}
        if isinstance(detail, ReturnDict):
            return ReturnDict(ret, serializer=detail.serializer)
        return ret

    text = force_str(detail)
    code = getattr(detail, "code", code)
    return ErrorDetail(code, text)


def _get_codes(detail):
    if isinstance(detail, list):
        return [_get_codes(item) for item in detail]
    elif isinstance(detail, dict):
        return {key: _get_codes(value) for key, value in detail.items()}
    return detail.code


def _get_full_details(detail):
    if isinstance(detail, list):
        return [_get_full_details(item) for item in detail]
    elif isinstance(detail, dict):
        return {key: _get_full_details(value) for key, value in detail.items()}
    return {"code": detail.code, "message": detail}


class APIException(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_code = "error"
    default_detail = _("A server error occurred.")

    def __init__(self, code=None, detail=None):
        if code is None:
            code = self.default_code
        if detail is None:
            detail = self.default_detail

        self.detail = _get_error_details(code=code, detail=detail)

    def __str__(self):
        return str(self.detail)

    def get_codes(self):
        return _get_codes(self.detail)

    def get_full_details(self):
        return _get_full_details(self.detail)


class BadRequest(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_code = "BAD_REQUEST"
    default_detail = "잘못된 요청입니다."


class NotAuthenticated(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_code = "NOT_AUTHENTICATED"
    default_detail = "로그인이 필요합니다."


class PermissionDenied(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_code = "PERMISSION_DENIED"
    default_detail = "권한이 없습니다."


class NotFound(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = "NOT_FOUND"
    default_detail = "해당 자원을 찾을 수 없습니다."
