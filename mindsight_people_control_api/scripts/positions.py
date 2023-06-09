"""This module provide methods to work with positions entity"""

from datetime import date, datetime

from mindsight_people_control_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_POSITIONS,
    DATE_FORMAT,
    DATETIME_FORMAT,
)


class Positions(ApiEndpoint):
    """This class abstract the positions endpoint methods
    Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_POSITIONS)

    def get_list_positions(
        self,
        name: str = None,
        code: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        active: str = None,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get positions data
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos/operation/listPositions

        Args:
            name (str, Optional): Position name
            code (str, Optional): Code of position
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            active (str, Optional): is_active: Flag to get positions by status
            search: search
            }
        """

        path = ""
        parameters = {
            "name": name,
            "code": code,
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
            "active": active,
            "search": search,
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def get_retrieve_position(
        self,
        _id: int,
        name: str = None,
        code: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        active: str = None,
        search: str = None,
    ) -> dict:
        """Get retrieve position
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos/operation/retrievePosition

        Args:
            _id (int, Mandatory): Id of position to retrieve
            name (str, Optional): Name of position
            code (str, Optional): Code of position
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            active (str, Optional): is_active: Flag to get positions by status
            search (str, Optional): search
        """
        path = f"/{_id}"

        parameters = {
            "name": name,
            "code": code,
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
            "active": active,
            "search": search,
        }
        return self._base_requests.get(
            path=path,
            parameters=parameters,
        )

    def post_create_position(
        self,
        code: str,
        name: str,
        start_date: date,
        category: str = None,
        description: str = None,
    ):
        """Create new position
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos/operation/createCompletePosition

        Args:
            code (str, Mandatory): Code of position
            name (str, Mandatory): Name of position
            start_date (date, Mandatory): Position start date
            category (str, Optional): Position category
            description (str, Optional): Position description
        """
        path = "/create_complete"
        data = {
            "code": code,
            "name": name,
            "start_date": start_date.strftime(DATE_FORMAT),
            "category": category,
            "description": description,
        }

        return self._base_requests.post(path=path, json=data)

    def patch_edit_position(
        self,
        _id: int,
        code: str = None,
        name: str = None,
        category: str = None,
        description: str = None,
        start_date: date = None,
        end_date: date = None,
    ) -> dict:
        """Edit position and last position record
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos/operation/editPositionAndRecordPosition

        Args:
            _id (int, Mandatory): Position id
            code (str, Optional): Code of position
            name (str, Optional): Name of position
            category (str, Optional): Category of position
            description (str, Optional): Description of position
            start_date (date, Optional): Position start date
            end_date (date, Optional): Position end date
        """
        path = f"/{_id}/edit_position_and_record"
        data = {
            "code": code,
            "name": name,
            "category": category,
            "description": description,
            "start_date": start_date.strftime(DATE_FORMAT) if start_date else None,
            "end_date": end_date.strftime(DATE_FORMAT) if end_date else None,
        }
        return self._base_requests.patch(path=path, data=data)
