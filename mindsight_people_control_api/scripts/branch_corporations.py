"""This module provide methods to work with areas entity"""

from datetime import datetime
from mindsight_people_control_api.utils.aux_functions import generate_url
from mindsight_people_control_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_BRANCH_CORPORATIONS,
    API_ENDPOINT_CORPORATIONS,
    DATETIME_FORMAT,
)

class BranchCorporations(ApiEndpoint):
    """This class abstract the branch corporation endpoint methods
    Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Filiais
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_BRANCH_CORPORATIONS)

    def get_list_branch_corporations(
        self,
        name__iexact: str = None,
        code: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
        expand: str = None,
    ) -> ApiPaginationResponse:
        """Get branch_corporations data
        https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Filiais/operation/listBranchCorporations

        Args:
            name__iexact (str, Optional): name__iexact
            code (str, Optional): Code of corporation
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            search (str, Optional): A search term.
            expand: (str, Optional): Possible to expand these fields in the response: uuid, branchs_corporation
        """

        path = ""
        parameters = {
            "name__iexact": name__iexact,
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
            "expand": expand,
            "search": search,
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def get_retrieve_branch_corporation(
        self,
        _id: int,
        name__iexact: str = None,
        code: str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
        expand: str = None,
    ) -> dict:
        """Get retrieve corporation
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Filiais/operation/retrieveBranchCorporation

        Args:
            name__iexact (str, Optional): name__iexact
            code (str, Optional): Code of corporation
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            search (str, Optional): A search term.
            expand: (str, Optional): Possible to expand these fields in the response: corporation, uuid
        """
        path = f"/{_id}"

        parameters = {
            "name__iexact": name__iexact,
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
            "expand": expand,
            "search": search,
            "page_size": self.page_size,
        }
        return self._base_requests.get(
            path=path,
            parameters=parameters,
        )

    def post_create_branch_corporation(
        self,
        code: str,
        name: str,
        corporation_id: str,
    ):
        """Create new area
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Filiais/operation/createBranchCorporation

        Args:
            code (str, Mandatory): Code of corporation
            name (str, Mandatory): Name of corporation
        """
        path = ""
        data = {
            "code": code,
            "name": name,
            "corporation": corporation_id
        }

        return self._base_requests.post(path=path, json=data)

    def patch_update_branch_corporation(
        self,
        _id: int,
        name: str,
        code: str,
        corporation_id: str,
        name__iexact: str = None,
        code_query:  str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> dict:
        """Partial update branch corporation
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Filiais/operation/partialUpdateBranchCorporation

        Args:
            _id (int, Mandatory): Branch Corporation id
            name (str, Mandatory): New branch corporation name
            code (str, Mandatory): New branch corporation code
            corporation_id (str, Mandatory): New corporation code
            name__iexact (str, Optional): name__iexact
            code_query (str, Optional): Code of corporation
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            search (str, Optional): A search term.
        """
        path = f"/{_id}"
        parameters = {
            "name__iexact": name__iexact,
            "code": code_query,
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
        data = {
            "code": code,
            "name": name,
            "corporation": corporation_id
        }
        return self._base_requests.patch(path=path, parameters=parameters, json=data)

    def put_edit_branch_corporation(
        self,
        _id: int,
        name: str,
        code: str,
        corporation_id: str,
        name__iexact: str = None,
        code_query:  str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> dict:
        """Partial edit branch corporation
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Filiais/operation/updateBranchCorporation

        Args:
            _id (int, Mandatory): Corporation id
            name (str, Mandatory): New branch corporation name
            code (str, Mandatory): New branch corporation code
            corporation_id (str, Mandatory): New corporation code
            name__iexact (str, Optional): name__iexact
            code_query (str, Optional): Code of corporation
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            search (str, Optional): A search term.
        """
        path = f"/{_id}"
        parameters = {
            "name__iexact": name__iexact,
            "code": code_query,
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
        data = {
            "code": code,
            "name": name,
            "corporation": corporation_id
        }
        return self._base_requests.put(path=path, parameters=parameters, json=data)
    
    def delete_branch_corporation(
        self,
        _id: int,
        name__iexact: str = None,
        code:  str = None,
        created__gt: datetime = None,
        created__lt: datetime = None,
        modified__gt: datetime = None,
        modified__lt: datetime = None,
        search: str = None,
    ) -> dict:
        """Delete corporation
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Empresas/operation/destroyCorporation

        Args:
            _id (int, Mandatory): Corporation id
            name__iexact (str, Optional): name__iexact
            code_query (str, Optional): Code of corporation
            created__gt (datetime, Optional): Datetime to apply filter ">=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            created__lt (datetime, Optional): Datetime to apply filter "<=" on created dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__gt (datetime, Optional): Datetime to apply filter ">=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            modified__lt (datetime, Optional): Datetime to apply filter "<=" on modified dates.
                Format "%Y-%m-%d %H:%M:%S"
            search (str, Optional): A search term.
        """
        path = f"/{_id}"
        parameters = {
            "name__iexact": name__iexact,
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
            "search": search,
        }
        return self._base_requests.delete(path=path, parameters=parameters)