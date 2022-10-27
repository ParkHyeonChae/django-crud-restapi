from apps.boards.models.boards import Board


def board_serializer(board: Board) -> dict:
    """board serializer"""

    return {"id": board.id, "name": board.name}
