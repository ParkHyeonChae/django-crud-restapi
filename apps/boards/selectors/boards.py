from typing import Optional

from apps.boards.models import Board
from django.db.models import QuerySet


def get_board_queryset() -> QuerySet[Optional[Board]]:
    """board queryset selector"""

    return Board.objects.only("name", "is_published").filter(is_published=True)
