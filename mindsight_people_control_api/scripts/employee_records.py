from datetime import datetime

from mindsight_people_control_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_EMPLOYEE_RECORDS,
    API_ENDPOINT_EMPLOYEES,
    DATETIME_FORMAT,
)
from mindsight_people_control_api.utils.aux_functions import generate_url


class EmployeeRecord(ApiEndpoint):
    """This class abstract the employee records endpoint methods
    Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-do-funcionario
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_EMPLOYEE_RECORDS)

    def get_list_employees_records(
        self,
        employee_id: int = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get employees records data
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-do-funcionario/operation/retrieveEmployeeRecord

        Args:
            employee_id (int, Optional): Employee id
            created__gt (str, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (str, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (str, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (str, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            active (str, Optional): is_active: Flag to get areas by status
            search: A search term.
        """

        path = ""
        parameters = {
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
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def get_retrieve_employee_record(
        self,
        _id: int,
        employee_id: int = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> dict:
        """Get employees records data
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-do-funcionario/operation/retrieveEmployeeRecord

        Args:
            _id (int, Optional): A unique integer value identifying employee record
            employee_id (int, Optional): Employee id
            created__gt (str, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (str, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (str, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (str, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            active (str, Optional): is_active: Flag to get areas by status
            search: A search term.
        """

        path = f"/{_id}"

        parameters = {
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
