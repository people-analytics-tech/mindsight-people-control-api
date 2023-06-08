from typing import Any, Literal

import requests

from mindsight_people_control_api.helpers.exceptions import BadRequestException
from mindsight_people_control_api.settings import API_TOKEN
from mindsight_people_control_api.utils.aux_functions import generate_url


class ApiPaginationResponse:
    count: int
    next: str
    previous: str
    results: list = []

    def __init__(self, **kwargs) -> None:
        self.count = kwargs["count"]
        self.next = kwargs["next"]
        self.previous = kwargs["previous"]
        self.results.extend(kwargs["results"])
        self.__headers = kwargs.get("headers")

    def get_all(self):
        if self.next:
            response = requests.get(url=self.next, headers=self.__headers)

            response.raise_for_status()
            response_data = response.json()

            self.results.extend(response_data["results"])
            self.count = response_data["count"]
            self.next = response_data["next"]
            self.previous = response_data["previous"]

            if self.next:
                self.get_all()

        return self


class BaseRequests:
    def __init__(self):
        self.__TOKEN = API_TOKEN
        self.BASE_PATH = "/"
        self.__headers = None

    def __authorization_header(self) -> dict:
        return {
            "Authorization": f"Token {self.__TOKEN}",
            "Content-Type": "application/json",
        }

    @staticmethod
    def __get_not_none_data_values(data: dict):
        result = {}
        for key, value in data.items():
            if value is not None:
                result[key] = value

        return result

    def __check_response(self, response: requests.Response):
        content_text = response.text
        try:
            response.raise_for_status()

        except requests.HTTPError:

            if response.status_code == 400:
                raise BadRequestException(message=content_text)

            else:
                raise response.raise_for_status()

        except Exception as e:
            raise e

    def __request_helper(
        self,
        path: str,
        method: Literal["get", "post", "put", "patch", "delete"],
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
        json: Any = None,
    ):
        if not headers:
            headers = {}

        request_url = generate_url(base_path=self.BASE_PATH, path=path)
        self.__headers = {**self.__authorization_header(), **headers}

        response = None
        method = method.lower()

        if method == "get":
            response = requests.get(
                url=request_url,
                headers=self.__headers,
                params=parameters,
                data=data,
            )

        elif method == "post":
            response = requests.post(
                url=request_url,
                headers=self.__headers,
                params=parameters,
                data=data,
                json=json,
            )

        elif method == "put":
            response = requests.put(
                url=request_url,
                headers=self.__headers,
                params=parameters,
                data=data,
                json=json,
            )

        elif method == "patch":
            response = requests.patch(
                url=request_url,
                headers=self.__headers,
                params=parameters,
                data=data,
                json=json,
            )

        elif method == "delete":
            response = requests.delete(
                url=request_url,
                headers=self.__headers,
                params=parameters,
                data=data,
                json=json,
            )

        # Check response
        self.__check_response(response)

        if (type(response) is not list) & (response is not None):
            response_json = response.json()

        if response_json.get("count") and response_json.get("next"):
            return ApiPaginationResponse(**response_json, headers=self.__headers)

        return response_json

    def get(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
    ):
        return self.__request_helper(
            path=path, method="get", headers=headers, parameters=parameters
        )

    def post(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
        json: Any = None,
    ) -> Any:
        return self.__request_helper(
            path=path,
            method="post",
            headers=headers,
            parameters=parameters,
            data=data,
            json=json,
        )

    def put(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
    ):
        return self.__request_helper(
            path=path,
            method="put",
            headers=headers,
            parameters=parameters,
            data=data,
        )

    def patch(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
    ):
        return self.__request_helper(
            path=path,
            method="patch",
            headers=headers,
            parameters=parameters,
            data=self.__get_not_none_data_values(data),
        )

    def delete(
        self,
        path: str,
        headers: dict = None,
        parameters: dict = None,
        data: Any = None,
    ):
        return self.__request_helper(
            path=path,
            method="delete",
            headers=headers,
            parameters=parameters,
            data=data,
        )
