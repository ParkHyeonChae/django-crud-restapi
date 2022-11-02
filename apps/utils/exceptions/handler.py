from apps.utils.exceptions import classes as custom_exceptions
from rest_framework.response import Response
from rest_framework.views import exceptions as origin_exceptions
from rest_framework.views import set_rollback


def api_exception_handler(exc, context):
    if isinstance(
        exc, (custom_exceptions.APIException, origin_exceptions.APIException)
    ):
        headers = {}
        if getattr(exc, "auth_header", None):
            headers["WWW-Authenticate"] = exc.auth_header
        if getattr(exc, "wait", None):
            headers["Retry-After"] = "%d" % exc.wait

        set_rollback()
        error = exc.get_full_details()
        error_response_data = {
            "code": error.get("code"),
            "message": error.get("message"),
        }
        return Response(
            data={"error": error_response_data}, status=exc.status_code, headers=headers
        )
    return None
