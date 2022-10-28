REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ),
    "EXCEPTION_HANDLER": "config.exceptions.api_exception_handler",
}
