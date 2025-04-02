import json
from fetch_data import get_source_id, get_target_id
from config import base_url
from http_methods import DELETE, POST


def filter_status_ids(file: str) -> list:
    with open(file) as json_file:
        text = json.load(json_file)
        statuses = text.get("values", [])
    status_ids = [status.get("id") for status in statuses]
    return status_ids


def delete_statuses(status_ids: list):
    url = base_url + "/rest/api/3/statuses"

    headers = {
      "Accept": "application/json"
    }

    statuses = "&".join(status_ids)

    query = {
      'id': statuses
    }

    DELETE(url, headers, query)


def delete_target_statuses():
    status_ids = filter_status_ids("target-statuses.json")
    delete_statuses(status_ids)





def create_statuses(project_id: int, statuses: list):
    url = base_url + "/rest/api/3/statuses"

    headers = {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
    
    scope = {
        "project":{
            "id": f'{project_id}'
        },
        "type": "PROJECT"
    }

    payload = json.dumps( {
        "scope": scope,
        "statuses": statuses
    })

    POST(url, headers, data=payload)
