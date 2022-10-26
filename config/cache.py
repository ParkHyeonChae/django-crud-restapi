import os

CACHE_BACKEND_URL = os.environ.get("CACHE_BACKEND_URL", None)

if CACHE_BACKEND_URL:
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": CACHE_BACKEND_URL,
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "IGNORE_EXCEPTIONS": True,
            },
        }
    }
