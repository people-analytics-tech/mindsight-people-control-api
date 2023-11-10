"""This module provide methods to work with employees entity"""

from datetime import date, datetime
from typing import Literal

from mindsight_people_control_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_AREAS,
    API_ENDPOINT_EMPLOYEES,
    API_ENDPOINT_POSITIONS,
    DATE_FORMAT,
    API_ENDPOINT_CORPORATIONS,
    API_ENDPOINT_BRANCH_CORPORATIONS,
)
from mindsight_people_control_api.utils.aux_functions import generate_url


class Employees(ApiEndpoint):
    """This class abstract the employees endpoint methods
    Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_EMPLOYEES)

    def get_list_employees(
        self,
        first_name: str = None,
        last_name: str = None,
        email: str = None,
        employee_code: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        active: str = None,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get areas data
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/listEmployees

        Args:
            first_name (str, Optional): Employee first name
            last_name (str, Optional): Employee last name
            email (str, Optional): Employee email
            employee_code (str, Optional): Employee code
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
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "employee_code": employee_code,
            "created__gt": created__gt,
            "created__lt": created__lt,
            "modified__gt": modified__gt,
            "modified__lt": modified__lt,
            "active": active,
            "search": search,
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def get_retrieve_employee(
        self,
        _id: int,
        first_name: str = None,
        last_name: str = None,
        email: str = None,
        employee_code: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        active: str = None,
        search: str = None,
    ) -> dict:
        """Get retrieve employee register
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/retrieveEmployee

        Args:
            _id (int, Mandatory): Id of employee to retrieve
            first_name (str, Optional): Employee first name
            last_name (str, Optional): Employee last name
            email (str, Optional): Employee email
            employee_code (str, Optional): Employee code
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
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "employee_code": employee_code,
            "created__gt": created__gt,
            "created__lt": created__lt,
            "modified__gt": modified__gt,
            "modified__lt": modified__lt,
            "active": active,
            "search": search,
        }
        return self._base_requests.get(
            path=path,
            parameters=parameters,
        )

    def post_create_employee(
        self,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        employee_code: str,
        start_date: date,
        area: int = None,
        position: int = None,
        manager: int = None,
        gender: str = None,
        cpf: str = None,
        birth_date: str = None,
        company_referal: str = None,
        work_type: str = None,  # "hybrid" "inoffice" "remote" "unknown"
        work_city: str = None,
        systems_permissions: list = None,
        corporation: int = None,
        branch_corporation: int = None,
    ):
        """Create new employee
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/createCompleteEmployee

        Args:
            first_name (str, Mandatory): Employee first name with 200 characters or fewer
            last_name (str, Mandatory): Employee last name with 200 characters or fewer
            username (str, Mandatory): Username with 254 characters or fewer. Letters,
                digits and @/./+/-/_ only
            email (str, Mandatory): Employee email
            employee_code (str, Mandatory): The employee code
            start_date (date, Mandatory): Start date of employee
            area (int, Optional): Employee area id
            position (int, Optional): Employee position id
            manager (int, Optional): Employee manager id
        """
        path = "/create_complete"
        data = {
            "first_name": first_name,
            "last_name": last_name,
            "username": username,
            "email": email,
            "employee_code": employee_code,
            "start_date": start_date.strftime(DATE_FORMAT),
            "area": generate_url(base_path=API_ENDPOINT_AREAS, path=f"/{area}")
            if area
            else area,
            "position": generate_url(
                base_path=API_ENDPOINT_POSITIONS, path=f"/{position}"
            )
            if position
            else position,
            "manager": generate_url(
                base_path=API_ENDPOINT_EMPLOYEES, path=f"/{manager}"
            )
            if manager
            else manager,
            "gender": gender,
            "cpf": cpf,
            "birth_date": birth_date,
            "company_referal": company_referal,
            "work_type": work_type,
            "work_city": work_city,
            "systems_permissions": systems_permissions,
            "corporation": generate_url(
                base_path=API_ENDPOINT_CORPORATIONS, path=f"/{corporation}"
            )
            if corporation
            else corporation,
            "branch_corporation": generate_url(
                base_path=API_ENDPOINT_BRANCH_CORPORATIONS,
                path=f"/{branch_corporation}",
            )
            if branch_corporation
            else branch_corporation,
        }

        return self._base_requests.post(path=path, json=data)

    def post_activate_employee(
        self,
        _id: int,
        start_date: date,
        area: int = None,
        position: int = None,
        manager: int = None,
    ):
        """Activate employee
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/activateEmployee

        Args:
            _id (int, Mandatory): Id of employee
            start_date (date, Mandatory): Start date of employee
            area (int, Optional): Employee area id
            position (int, Optional): Employee position id
            manager (int, Optional): Employee manager id
        """
        path = f"{_id}/activate"

        data = {
            "start_date": start_date.strftime(DATE_FORMAT),
            "area": generate_url(base_path=API_ENDPOINT_AREAS, path=f"/{area}"),
            "position": generate_url(
                base_path=API_ENDPOINT_POSITIONS, path=f"/{position}"
            ),
            "manager": generate_url(
                base_path=API_ENDPOINT_EMPLOYEES, path=f"/{manager}"
            ),
        }

        return self._base_requests.post(path=path, json=data)

    def post_deactivate_employee(
        self,
        _id: int,
        end_date: date,
        termination_type: Literal[
            "dismissed", "resigned", "transfer", "intern_to_full", "others"
        ] = "others",
        termination_reason: str = None,
    ):
        """Deactivate employee
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/deactivateEmployee

        Args:
            _id (int, Mandatory): Id of employee
            end_date (date, Mandatory): Start date of employee
            termination_type (str, Optional): Termination type, default "others"
            termination_reason (str, Optional): Termination reason
        """
        path = f"{_id}/deactivate"

        data = {
            "end_date": end_date.strftime(DATE_FORMAT),
            "termination_type": termination_type,
            "termination_reason": termination_reason,
        }

        return self._base_requests.post(path=path, json=data)

    def get_retrieve_current_area(self, _id: int) -> dict:
        """Retrieve employee current area record
        Args:
            _id (int, Mandatory): Employee id
        """
        path = f"/{_id}/current_area"

        return self._base_requests.get(path=path)

    def post_change_current_area(
        self, _id: int, area_id: int, start_date: date, review_access: bool = False
    ) -> dict:
        """Change employee current area
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/changeCurrentAreaEmployee

        Args:
            _id (int, Mandatory): Employee id
            area_id (int, Mandatory): New employee area id
            review_access (bool, Optional): Mark if this change will have review access
        """
        path = f"/{_id}/current_area"

        payload = {
            "area": generate_url(base_path=API_ENDPOINT_AREAS, path=f"/{area_id}"),
            "start_date": start_date.strftime(DATE_FORMAT),
            "review_access": review_access,
        }

        return self._base_requests.post(path=path, json=payload)

    def get_retrieve_current_manager(self, _id: int) -> dict:
        """Retrieve employee current manager record
        Args:
            _id (int, Mandatory): Employee id
        """
        path = f"/{_id}/current_manager"

        return self._base_requests.get(path=path)

    def post_change_current_manager(
        self, _id: int, manager_id: int, start_date: date, review_access: bool = False
    ) -> dict:
        """Change employee current manager
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/changeManagerEmployee

        Args:
            _id (int, Mandatory): Employee id
            manager_id (int, Mandatory): New employee manager id
            review_access (bool, Optional): Mark if this change will have review access
        """
        path = f"/{_id}/current_manager"

        payload = {
            "manager": generate_url(
                base_path=API_ENDPOINT_EMPLOYEES, path=f"/{manager_id}"
            ),
            "start_date": start_date.strftime(DATE_FORMAT),
            "review_access": review_access,
        }

        return self._base_requests.post(path=path, json=payload)

    def get_retrieve_current_position(self, _id: int) -> dict:
        """Retrieve employee current position record
        Args:
            _id (int, Mandatory): Employee id
        """
        path = f"/{_id}/current_position"

        return self._base_requests.get(path=path)

    def post_change_current_position(
        self, _id: int, position_id: int, start_date: date, review_access: bool = False
    ) -> dict:
        """Change employee current position
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Funcionarios/operation/changePositionEmployee

        Args:
            _id (int, Mandatory): Employee id
            position_id (int, Mandatory): New employee position id
            review_access (bool, Optional): Mark if this change will have review access
        """
        path = f"/{_id}/current_position"

        payload = {
            "position": generate_url(
                base_path=API_ENDPOINT_POSITIONS, path=f"/{position_id}"
            ),
            "start_date": start_date.strftime(DATE_FORMAT),
            "review_access": review_access,
        }

        return self._base_requests.post(path=path, json=payload)
