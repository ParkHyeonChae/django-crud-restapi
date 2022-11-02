REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": (),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "EXCEPTION_HANDLER": "apps.utils.exceptions.handler.api_exception_handler",
}
