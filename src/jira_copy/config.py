

from requests.auth import HTTPBasicAuth

# The base URL of your instance
base_url = "https://kv-sdlc-test.atlassian.net"

# Pass the key of the source project you want to clone
source_project_key = 'TSP'

# Set the name and key of the new project
target_project_key = 'TTP'

# Pass your username for authenitcation
username = ""

# Pass your API key for authentiction
api_key = ""

# Set the authentication credentials using HTTP Basic Authentication
authentication = HTTPBasicAuth(username, api_key)
