from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    """user manager"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is False:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is False:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class User(PermissionsMixin, AbstractBaseUser):
    """user model"""

    objects = UserManager()
    USERNAME_FIELD = "email"

    email = models.CharField(unique=True, db_index=True, max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    dormanted_at = models.DateTimeField(null=True)
    deactivated_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateTimeField()

    class Meta:
        db_table = "user"
        verbose_name_plural = "User (사용자)"
