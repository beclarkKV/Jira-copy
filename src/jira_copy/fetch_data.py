from http_methods import GET
from config import base_url, source_project_key, target_project_key
import json

def get_project_json(key: str) -> dict:
    url = base_url + f"/rest/api/3/project/{key}"
    headers = {
    "Accept": "application/json"
    }
    response = GET(url, headers)

    return response.json()

def get_project_id(key: str) -> int:
    return get_project_json(key).get("id")

def get_project_issue_types(project_id: int) -> dict:
    url = base_url + "/rest/api/3/issuetype/project"

    headers = {
        "Accept": "application/json"
    }

    query = {
        'projectId': f'{project_id}'
    }

    response = GET(url, headers, query)

    return response.json()

def get_source_issue_types():
    project_id = get_project_id(source_project_key)
    response = get_project_issue_types(project_id)
    with open('source-issue-types.json', 'w') as source_file:
        json.dump(response, source_file, indent=4)
    
def get_target_issue_types():
    project_id = get_project_id(target_project_key)
    response = get_project_issue_types(project_id)
    with open('target-issue-types.json', 'w') as target_file:
        json.dump(response, target_file, indent=4)    

def get_project_statuses(project_id: int ) -> dict:
    url = base_url + "/rest/api/3/statuses/search"

    headers = {
      "Accept": "application/json"
    }

    params = {"projectId": project_id}

    response = GET(url, headers, params)

    return response.json()

def get_source_statuses():
    project_id = get_project_id(source_project_key)
    response = get_project_statuses(project_id)
    with open("source-statuses.json", "w") as source_file:
        json.dump(response, source_file, indent=4)

def get_target_statuses():
    project_id = get_project_id(target_project_key)
    response = get_project_statuses(project_id)
    with open("target-statuses.json", "w") as target_file:
        json.dump(response, target_file, indent=4)

