from mindsight_people_control_api.settings import API_BASE_URL, API_VERSION


def generate_url(base_path: str, path: str) -> str:
    return f"{API_BASE_URL}/{API_VERSION}{base_path}{path}/"
