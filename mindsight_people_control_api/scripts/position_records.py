"""This module provide methods to work with position records entity"""
from mindsight_people_control_api.helpers.models import (
    ApiEndpoint,
    ApiPaginationResponse,
)
from mindsight_people_control_api.settings import (
    API_ENDPOINT_POSITION_RECORDS,
)


class PositionRecords(ApiEndpoint):
    """This class abstract the positions records endpoint methods
    Reference: https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-de-cargo
    """

    def __init__(self) -> None:
        super().__init__(API_ENDPOINT_POSITION_RECORDS)

    def get_list_position_records(
        self,
        position: str = None,
        search: str = None,
    ) -> ApiPaginationResponse:
        """Get positions data
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-de-cargo/operation/listPositionRecords

        Args:
            position (str, Optional): Positon name
            search: search
        """

        path = ""
        parameters = {
            "position": position,
            "search": search,
            "page_size": self.page_size,
        }
        return ApiPaginationResponse(
            **self._base_requests.get(path=path, parameters=parameters),
            headers=self._base_requests.headers,
        )

    def get_retrieve_positon_record(
        self,
        _id: int,
        position: str = None,
        search: str = None,
    ) -> dict:
        """Get retrieve area
        Reference:
            https://controle.mindsight.com.br/stone/api/v1/docs/#tag/Registros-de-cargo/operation/retrievePositionRecord

        Args:
            _id (int, Mandatory): A unique integer value identifying this record of position.
            position (str, Optional): Position name
            search (str, Optional): search
        """
        path = f"/{_id}"

        parameters = {
            "position": position,   
            "search": search,
        }
        return self._base_requests.get(
            path=path,
            parameters=parameters,
        )
