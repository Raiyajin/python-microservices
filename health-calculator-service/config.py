import logging
import os
import requests


def get_version() -> str:
    """
    Get the version of the application from the GitHub API.
    :return:
    """
    version = "0.1.0"
    try:
        res = requests.get(os.getenv("GITHUB_RELEASE_API_URL"))
        if res.status_code != 200:
            raise requests.RequestException

        version = res.json()["tag_name"]

    except requests.RequestException as e:
        logging.warning(f"Warning: couldn't fetch version from github: {e}")

    return version

SWAGGER_CONFIG = {
    "headers": [],
    "specs": [
        {
            "title": "Health Calculator API",
            "version": get_version(),
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/"
}

