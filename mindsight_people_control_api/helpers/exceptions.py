"""Module providing exceptions structure"""


class PeopleControlExceptions(Exception):
    """People control api base exceptions"""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class BadRequestException(PeopleControlExceptions):
    """Bad Request From api"""

    def __init__(self, message: str) -> None:
        super().__init__(f"ERROR: {message}")

class ServerErrorException(PeopleControlExceptions):
    """Bad Request From api"""

    def __init__(self, message: str) -> None:
        super().__init__(f"ERROR: {message}")
