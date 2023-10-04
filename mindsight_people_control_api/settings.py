"""This module define project configurations variables"""

from decouple import config

# API Constants
API_TOKEN = config("MINDSIGHT_CP_API_TOKEN")
API_BASE_URL = config("MINDSIGHT_CP_API_URL")
API_VERSION = "v1"

# Request config
PAGE_SIZE: int = 1000
TIMEOUT: int = 600  # Default set to 600 seconds (10 minutes)

# Date formats
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
DATE_FORMAT = "%Y-%m-%d"

# Endpoints
API_ENDPOINT_EMPLOYEES = "/employees"
API_ENDPOINT_EMPLOYEE_RECORDS = "/employee_records"
API_ENDPOINT_AREAS = "/areas"
API_ENDPOINT_AREAS_RECORDS = "/area_records"
API_ENDPOINT_PARENT_AREAS = "/parent_areas"
API_ENDPOINT_EMPLOYEE_AREAS = "/employee_areas"
API_ENDPOINT_EMPLOYEE_POSITIONS = "/employee_positions"
API_ENDPOINT_EMPLOYEE_MANAGERS = "/employee_managers"
API_ENDPOINT_USERS = "/users"
API_ENDPOINT_POSITIONS = "/positions"
API_ENDPOINT_POSITION_RECORDS = "/position_records"
API_ENDPOINT_CORPORATIONS = "/corporations"
API_ENDPOINT_BRANCH_CORPORATIONS = "/branch_corporations"
