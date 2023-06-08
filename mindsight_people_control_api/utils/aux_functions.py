"""This module provide aux functions to distinct proposes"""

from mindsight_people_control_api.settings import API_BASE_URL, API_VERSION


def generate_url(base_path: str, path: str) -> str:
    """Aux function to generate a URL in Api format"""
    return f"{API_BASE_URL}/{API_VERSION}{base_path}{path}/"
