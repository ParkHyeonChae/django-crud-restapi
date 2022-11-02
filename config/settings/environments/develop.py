"""
development environments settings
"""

from config.settings import *  # noqa

DEBUG = True
ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = [
    "127.0.0.1",
]
CORS_ORIGIN_ALLOW_ALL = True
INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
)
ENVIRONMENT_NAME = "develop"
HTTP_PROTOCOL = "http"
SITE_DOMAIN = "localhost:8000"
SITE_URL = f"{HTTP_PROTOCOL}://{SITE_DOMAIN}"
