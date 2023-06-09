"""This module provide helpers classes to represent objects"""

import requests

from mindsight_people_control_api.helpers.base_requests import BaseRequests
from mindsight_people_control_api.settings import PAGE_SIZE, TIMEOUT


class ApiEndpoint:
    """This class represents a base api endpoint classes"""

    _base_requests: BaseRequests = BaseRequests()

    def __init__(self, base_path: str) -> None:
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

    def get_all(self):
        """Get all pages of data"""
        if self.next:
            response = requests.get(
                url=self.next,
                headers=self.__headers,
                timeout=TIMEOUT,
            )

            response.raise_for_status()
            response_data = response.json()

            self.results.extend(response_data["results"])
            self.count = response_data["count"]
            self.next = response_data["next"]
            self.previous = response_data["previous"]

            if self.next:
                self.get_all()

        return self
