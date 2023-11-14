"""This module provide helpers classes to represent objects"""

from time import sleep

import requests

from mindsight_people_control_api.helpers.base_requests import BaseRequests
from mindsight_people_control_api.settings import PAGE_SIZE, TIMEOUT


class Timeout(object):
    """This class is aux to manage timeout between classes in module."""

    _timeout: int = TIMEOUT

    @property
    @classmethod
    def timeout(cls) -> int:
        """Get timeout setted."""
        return cls._timeout

    @timeout.setter
    @classmethod
    def timeout(cls, value: int):
        """Set timeout value."""
        cls._timeout = value


class ApiEndpoint:
    """This class represents a base api endpoint classes"""

    def __init__(self, base_path: str) -> None:
        self._base_requests: BaseRequests = BaseRequests()
        self._base_requests.base_path = base_path
        self._page_size: int = PAGE_SIZE

    @property
    def page_size(self) -> int:
        """Get number of records per page."""
        return self._page_size

    @page_size.setter
    def page_size(self, value: int):

        if value <= 0:
            raise ValueError("Page size can be > 0.")

        self._page_size = value

    @property
    def timeout(self) -> int:
        """Get timeout seconds."""
        return self._base_requests.timeout

    @timeout.setter
    def timeout(self, value: int):
        """Set timeout config to request."""
        if value <= 0:
            raise ValueError("Timeout can be > 0.")

        self._base_requests.timeout = value
        Timeout.timeout = value


class ApiPaginationResponse:
    """Class to work with paginated responses"""

    results: list = []

    def __init__(
        self,
        count: int,
        previous: str = None,
        results: list = None,
        headers: dict = None,
        **kwargs,
    ) -> None:
        self.count = count
        self.next = kwargs.get("next")
        self.previous = previous
        self.results.extend(results if results else [])
        self.__headers = headers
        self.timeout = Timeout.timeout if isinstance(Timeout.timeout, int) else Timeout._timeout

    def get_all(self, retries: int = 1):
        """Get all pages of data"""
        if self.next:
            try:
                response = requests.get(
                    url=self.next,
                    headers=self.__headers,
                    timeout=self.timeout,
                )
                response.raise_for_status()

            except Exception as error:
                if retries > 0:
                    print(f"Error on try get {self.next}: {error}")
                    print("Retry in 30s...")
                    sleep(30)
                    self.get_all(retries=retries - 1)

                else:
                    raise error

            response_data = response.json()

            self.results.extend(response_data["results"])
            self.count = response_data["count"]
            self.next = response_data["next"]
            self.previous = response_data["previous"]

            if self.next:
                self.get_all()

        return self
