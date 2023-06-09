"""This module provide methods to work with employee positions entity"""

from datetime import datetime

from mindsight_people_control_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_EMPLOYEE_POSITIONS,
    API_ENDPOINT_EMPLOYEES,
    API_ENDPOINT_POSITIONS,
    DATETIME_FORMAT,
)
from mindsight_people_control_api.utils.aux_functions import generate_url


class EmployeePositions(ApiEndpoint):
    """This class abstract the employee positions endpoint methods
    Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos-do-funcionario
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_EMPLOYEE_POSITIONS)

    def get_list_employee_positions(
        self,
        position_id: int = None,
        employee_id: int = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        active: str = None,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get employees records data
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos-do-funcionario/operation/listEmployeePositions

        Args:
            position_id (int, Optional): Position id
            employee_id (int, Optional): Employee id
            created__gt (str, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (str, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (str, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (str, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            active (str, Optional): is_active: Flag to get positions by status
            search: A search term.
        """

        path = ""
        parameters = {
            "position": (
                generate_url(base_path=API_ENDPOINT_POSITIONS, path=f"/{position_id}")
                if position_id
                else None
            ),
            "employee": (
                generate_url(base_path=API_ENDPOINT_EMPLOYEES, path=f"/{employee_id}")
                if employee_id
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
            "active": active,
            "search": search,
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def get_retrieve_employee_position_record(
        self,
        _id: int,
        position_id: int = None,
        employee_id: int = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> dict:
        """Get employee area record
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Cargos-do-funcionario/operation/retrieveEmployeePosition

        Args:
            _id (int, Optional): A unique integer value identifying employee position record
            position_id (int, Optional): Position id
            employee_id (int, Optional): Employee id
            created__gt (str, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (str, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (str, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (str, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            active (str, Optional): is_active: Flag to get position by status
            search: A search term.
        """

        path = f"/{_id}"

        parameters = {
            "position": (
                generate_url(base_path=API_ENDPOINT_POSITIONS, path=f"/{position_id}")
                if position_id
                else None
            ),
            "employee": (
                generate_url(base_path=API_ENDPOINT_EMPLOYEES, path=f"/{employee_id}")
                if employee_id
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
        return self._base_requests.get(path=path, parameters=parameters)
