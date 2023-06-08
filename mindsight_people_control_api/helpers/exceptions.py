class PeopleControlExceptions(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class BadRequestException(PeopleControlExceptions):
    def __init__(self, message: str) -> None:
        super().__init__(f"ERROR: {message}")
