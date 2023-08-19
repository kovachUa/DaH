import os
import requests
import json
import sys

def get_repositories(api_url):
    dname = '/json/git'
    name = api_url.split("/")[-1]
  
    api_url = f"https://api.github.com/orgs/{name}/repos"
   
    repositories = []

    def fetch_repositories(page=1):
        response = requests.get(f"{api_url}?page={page}")
        
        if response.status_code != 200:
            return

        try:
            data = response.json()
        except json.JSONDecodeError:
            return

        for item in data:
            repositories.append(item["html_url"])
  
        if data:
            fetch_repositories(page + 1)
    
    fetch_repositories()
  
    with open(f"{dname}/{name}.json", "w") as file:
        json.dump({"urls": repositories}, file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
    else:
        api_url = sys.argv[1]
        get_repositories(api_url)
