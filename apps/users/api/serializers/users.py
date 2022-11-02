from typing import Any, Dict

from apps.users.models.users import User


def user_serializer(user: User) -> Dict[str, Any]:
    """user serializer"""

    return {
        "id": user.id,
        "email": user.email,
        "isStaff": user.is_staff,
        "lastLogin": user.last_login,
        "createdAt": user.created_at,
    }
