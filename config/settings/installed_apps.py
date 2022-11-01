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
    "django_extensions",
    "corsheaders",
]

DOMAIN_APPS = [
    "apps.users",
    "apps.boards",
]

INSTALLED_APPS = DJANGO_APPS + LIBRARY_APPS + DOMAIN_APPS
