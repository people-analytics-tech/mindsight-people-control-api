# Mindsight People Control API
[![PyPI Latest Release](https://img.shields.io/pypi/v/mindsight-people-control-api.svg)](https://pypi.org/project/mindsight-people-control-api/)

Use mindsight people control functionalities in your python application.
## Instalation
```sh
pip install mindsight-people-control-api
```

# Configuration
## Environment variables
To use mindsight-people-control-api, you need to set two environment variables:
```dotenv
# ---DOTENV EXAMPLE---
MINDSIGHT_CP_API_TOKEN= # Token to authenticate
MINDSIGHT_CP_API_URL=https://controle.mindsight.com.br/api # Base path of your api instance
```
# Usage Example
You can use mindsight-people-control-api in order to create, update and delete registers on all system tables.

## List registers
You can use get methods to list registers of system table. See the following example:
```python
import mindsight_people_control_api


# Instantiate Areas client object
areas_client = mindsight_people_control_api.Areas()

# get_list_areas will return a ApiPaginationResponse object.
# This object represents a pagination response from rest api from people control
# and with get_all method from ApiPaginationResponse object, you can get all
# data of all pages. The data will stored in results attribute of ApiPaginationResponse

areas_data = areas_client.get_list_areas().get_all().results
```
