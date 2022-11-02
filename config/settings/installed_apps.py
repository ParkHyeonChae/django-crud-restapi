"""
installed apps
"""

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

LIBRARY_APPS = [
    "rest_framework",
    "rest_framework_jwt",
    "rest_framework.authtoken",
    "rest_auth",
    "django_extensions",
    "django_celery_results",
    "django_celery_beat",
    "corsheaders",
]

DOMAIN_APPS = [
    "apps.users",
    "apps.boards",
]

INSTALLED_APPS = DJANGO_APPS + LIBRARY_APPS + DOMAIN_APPS
