import json
from fetch_data import get_source_id, get_target_id
from config import base_url
from http_methods import DELETE

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
    with open("target-statuses.json") as target_file:
        text = json.load(target_file)
        statuses = text.get("values", [])
    status_ids = [status.get("id") for status in statuses]
    delete_statuses(status_ids)