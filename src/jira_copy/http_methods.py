from config import authentication
import requests
from requests import Response
import json




def GET(url: str, headers: dict={}, params: dict={}) -> Response:
    response = requests.request(
       "GET",
       url,
       headers=headers,
       auth=authentication,
       params=params
    )
    if response.status_code == 200:
        return response
    else:
        print(response.text)
        response.raise_for_status()

def POST(url:str, headers: dict={}, params: dict={}, data: dict={}) -> Response:
    response = requests.request(
        'POST',
        url,
        headers=headers,
        params=params,
        auth=authentication,
        data=json.dumps(data),
        )
    if response.status_code == 200:
        return response
    else:
        print(response.text)
        response.raise_for_status()

def DELETE(url:str, headers: dict={}, params: dict={}):
    response = requests.request(
        'DELETE',
        url,
        headers=headers,
        params=params,
        auth=authentication,
        )
    if response.status_code == 200:
        return response
    else:
        print(response.text)
        response.raise_for_status()
