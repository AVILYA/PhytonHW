import requests
import json


class YouGileApiClient:
    def __init__(self, base_url, token):  
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, name, description=None, code=None):
        url = f"{self.base_url}/projects"
        payload = {"name": name}
        if description:
            payload["description"] = description
        if code:
            payload["code"] = code
        response = requests.post(url, headers=self.headers, json=payload)
        try:
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.HTTPError as e:
            return response.json()
            

    def get_projects(self):
        url = f"{self.base_url}/projects"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_project(self, project_id, name=None, description=None, code=None):
        url = f"{self.base_url}/projects/{project_id}"
        payload = {}
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
        if code:
            payload["code"] = code
        response = requests.put(url, headers=self.headers, json=payload)
        try:
             response.raise_for_status()
             return response.json()
        except requests.exceptions.HTTPError as e:
            return response.json()


    def get_project(self, project_id):
        url = f"{self.base_url}/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()