"""This module provide methods to work with areas records entity"""
from datetime import datetime

from mindsight_people_control_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_AREAS,
    API_ENDPOINT_PARENT_AREAS,
    DATETIME_FORMAT,
)
from mindsight_people_control_api.utils.aux_functions import generate_url


class ParentAreas(ApiEndpoint):
    """This class abstract the areas records endpoint methods
    Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Areas-pai
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_PARENT_AREAS)

    def get_list_parent_areas(
        self,
        area_id: int = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get areas data
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Areas-pai/operation/listParentAreas

        Args:
            area_id (int, Optional): Area id
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            search: search
        """

        path = ""
        parameters = {
            "area": (
                generate_url(base_path=API_ENDPOINT_AREAS, path=f"/{area_id}")
                if area_id
                else None
            ),
            "created__gt": created__gt.strftime(DATETIME_FORMAT)
            if created__gt
            else None,
            "created__lt": created__lt.strftime(DATETIME_FORMAT)
            if created__lt
            else None,
            "modified__gt": modified__gt.strftime(DATETIME_FORMAT)
            if modified__gt
            else None,
            "modified__lt": modified__lt.strftime(DATETIME_FORMAT)
            if modified__lt
            else None,
            "search": search,
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def get_retrieve_parent_area(
        self,
        _id: int,
        area_id: int = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> dict:
        """Get retrieve parent area record
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Areas-pai/operation/retrieveParentArea

        Args:
            _id (int, Mandatory): A unique integer value identifying parent area record.
            area_id (str, Optional): Area id
            created__gt (str, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (str, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (str, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (str, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            search (str, Optional): search
        """
        path = f"/{_id}"

        parameters = {
            "area": (
                generate_url(base_path=API_ENDPOINT_AREAS, path=area_id)
                if area_id
                else None
            ),
            "created__gt": created__gt.strftime(DATETIME_FORMAT)
            if created__gt
            else None,
            "created__lt": created__lt.strftime(DATETIME_FORMAT)
            if created__lt
            else None,
            "modified__gt": modified__gt.strftime(DATETIME_FORMAT)
            if modified__gt
            else None,
            "modified__lt": modified__lt.strftime(DATETIME_FORMAT)
            if modified__lt
            else None,
            "search": search,
        }
        return self._base_requests.get(
            path=path,
            parameters=parameters,
        )
