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


def get_source_json():
    response = get_project_json(source_project_key)
    with open("source-project.json", "w") as source_file:
        json.dump(response, source_file, indent=4)


def get_target_json():
    response = get_project_json(target_project_key)
    with open("target-project.json", "w") as target_file:
        json.dump(response, target_file, indent=4)


def get_source_id():
    with open("source-project.json") as source_file:
        text = json.load(source_file)
        return text.get("id", -1)


def get_target_id():
    with open("target-project.json") as target_file:
        text = json.load(target_file)
        return text.get("id", -1)


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
    project_id = get_source_id()
    response = get_project_issue_types(project_id)
    with open('source-issue-types.json', 'w') as source_file:
        json.dump(response, source_file, indent=4)

    
def get_target_issue_types():
    project_id = get_target_id()
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
    project_id = get_source_id()
    response = get_project_statuses(project_id)
    with open("source-statuses.json", "w") as source_file:
        json.dump(response, source_file, indent=4)


def get_target_statuses():
    project_id = get_target_id()
    response = get_project_statuses(project_id)
    with open("target-statuses.json", "w") as target_file:
        json.dump(response, target_file, indent=4)

