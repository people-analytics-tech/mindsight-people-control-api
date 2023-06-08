from mindsight_people_control_api.helpers.base_requests import (
    ApiPaginationResponse,
    BaseRequests,
)
from mindsight_people_control_api.settings import API_ENDPOINT_AREAS_RECORDS, PAGE_SIZE


class AreaRecords:
    base_requests = BaseRequests()

    def __init__(self) -> None:
        self.base_requests.BASE_PATH = API_ENDPOINT_AREAS_RECORDS
        self.PAGE_SIZE = PAGE_SIZE

    def get_list_area_records(
        self,
        area: str = None,
        code: str = None,
        created__gt: str = None,
        created__lt: str = None,
        modified__gt: str = None,
        modified__lt: str = None,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get areas data
        Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-de-area/operation/listAreaRecords

        Args:
            area (str, Optional): Area name
            code (str, Optional): Code of area
            created__gt (str, Optional): Datetime to apply filter ">=" on created dates. Format "%Y-%m-%d %H:%M:%S"
            created__lt (str, Optional): Datetime to apply filter "<=" on created dates. Format "%Y-%m-%d %H:%M:%S"
            modified__gt (str, Optional): Datetime to apply filter ">=" on modified dates. Format "%Y-%m-%d %H:%M:%S"
            modified__lt (str, Optional): Datetime to apply filter "<=" on modified dates. Format "%Y-%m-%d %H:%M:%S"
            search: search
        """

        path = ""
        parameters = {
            "area": area,
            "code": code,
            "created__gt": created__gt,
            "created__lt": created__lt,
            "modified__gt": modified__gt,
            "modified__lt": modified__lt,
            "search": search,
            "page_size": self.PAGE_SIZE,
        }
        return self.base_requests.get(path=path, parameters=parameters)

    def get_retrieve_area_record(
        self,
        id: int,
        area: str = None,
        code: str = None,
        created__gt: str = None,
        created__lt: str = None,
        modified__gt: str = None,
        modified__lt: str = None,
        search: str = None,
    ) -> dict:
        """Get retrieve area
        Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-de-area/operation/retrieveAreaRecord

        Args:
            id (int, Mandatory): A unique integer value identifying this record of area.
            area (str, Optional): Area name
            code (str, Optional): Code of area
            created__gt (str, Optional): Datetime to apply filter ">=" on created dates. Format "%Y-%m-%d %H:%M:%S"
            created__lt (str, Optional): Datetime to apply filter "<=" on created dates. Format "%Y-%m-%d %H:%M:%S"
            modified__gt (str, Optional): Datetime to apply filter ">=" on modified dates. Format "%Y-%m-%d %H:%M:%S"
            modified__lt (str, Optional): Datetime to apply filter "<=" on modified dates. Format "%Y-%m-%d %H:%M:%S"
            search (str, Optional): search
        """
        path = f"/{id}"

        parameters = {
            "area": area,
            "code": code,
            "created__gt": created__gt,
            "created__lt": created__lt,
            "modified__gt": modified__gt,
            "modified__lt": modified__lt,
            "search": search,
        }
        return self.base_requests.get(
            path=path,
            parameters=parameters,
        )
