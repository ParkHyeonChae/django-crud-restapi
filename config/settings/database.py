"""
database config
"""

import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", None),
        "USER": os.environ.get("DB_USERNAME", None),
        "PASSWORD": os.environ.get("DB_PASSWORD", None),
        "HOST": os.environ.get("DB_HOSTNAME", None),
        "PORT": os.environ.get("DB_PORT", None),
    }
}
