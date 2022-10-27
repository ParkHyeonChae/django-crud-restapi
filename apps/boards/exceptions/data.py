from rest_framework.exceptions import APIException


class Http401NotAuthenticatedException(APIException):
    status_code = 401
    default_detail = "Required Login."


class Http400RequiredPostBodyException(APIException):
    status_code = 400
    default_detail = "Required Post Body."


class Http404NotFoundPostException(APIException):
    status_code = 404
    default_detail = "Not Found Post."
