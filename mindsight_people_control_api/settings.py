from decouple import config

# API Constants
API_TOKEN = config("MINDSIGHT_API_TOKEN")
API_BASE_URL = config("MINDSIGHT_API_BASE_URL")
API_VERSION = "v1"

# Request config
PAGE_SIZE = 1000

# Endpoints
API_ENDPOINT_EMPLOYEES = "/employees"
API_ENDPOINT_AREAS = "/areas"
API_ENDPOINT_AREAS_RECORDS = "/area_records"
API_ENDPOINT_EMPLOYEE_AREAS = "/employee_areas"
API_ENDPOINT_EMPLOYEE_MANAGERS = "/employee_manager"
