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

def get_issue_type_names(issue_types: list) -> list:
    issue_type_names = [issue_type["name"] for issue_type in issue_types]
    return issue_type_names

def compare_issue_types() -> dict:
    with open("source-issue-types.json") as source_file:
        source_json = json.load(source_file)
        source_names = set(get_issue_type_names(source_json))
    with open("target-issue-types.json") as target_file:
        target_json = json.load(target_file)
        target_names = set(get_issue_type_names(target_json))

    missing_types = source_names - target_names