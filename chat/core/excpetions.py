from fastapi.exceptions import HTTPException


class NotFoundException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=400,
            detail="Item not found"
        )