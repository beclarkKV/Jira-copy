import json

class IssueTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)


def filter_issue_type_names(issue_types: list) -> list:
    issue_type_names = [issue_type["name"] for issue_type in issue_types]
    return issue_type_names


def compare_issue_types():
    with open("source-issue-types.json") as source_file:
        source_json = json.load(source_file)
        source_names = set(filter_issue_type_names(source_json))
    with open("target-issue-types.json") as target_file:
        target_json = json.load(target_file)
        target_names = set(filter_issue_type_names(target_json))

    missing_types = source_names - target_names
    unexpected_types = target_names - source_names

    if missing_types != set():
        print(f"Source and target dont have same issue type names ERROR: target does not have issue types {missing_types}")
        raise IssueTypeError(f"Missing issue types: {missing_types}")
    if unexpected_types != set():
        print(f"Source and target dont have same issue type names ERROR: target has unexpected issue types {unexpected_types}")
        raise IssueTypeError(f"Unexpected issue types: {unexpected_types}")