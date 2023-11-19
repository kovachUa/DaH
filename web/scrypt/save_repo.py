import sys
import os
import requests
import json
from parse import parse

def get_github_repositories(username):
    # Construct the URL to fetch GitHub repositories for a given username
    url = f"https://api.github.com/users/{username}/repos"
    # Make a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response and return the list of repositories
        repositories = response.json()
        return repositories
    else:
        # If the request was not successful, return None
        return None

def extract_username_from_url(url):
    # Parse the GitHub URL to extract the username
    result = parse("https://github.com/{}", url)
    if result:
        # Split the result to get the username
        return result[0].split("/")[0]
    else:
        # Return None if the URL does not match the expected format
        return None

# Check if a GitHub URL is provided as a command-line argument
if len(sys.argv) != 2:
    # If not, exit the script with an error code
    sys.exit(1)

# Retrieve the GitHub URL provided by the user
github_url = sys.argv[1]

# Extract the username from the GitHub URL
username = extract_username_from_url(github_url)

if username:
    # Get the list of GitHub repositories for the specified username
    repositories = get_github_repositories(username)

    if repositories:
        # Save the repository URLs to a JSON file in the current directory
        output_filename = f"{username}.json"
        with open(output_filename, "w") as file:
            json.dump({"urls": [repo['html_url'] for repo in repositories]}, file, indent=2)

    else:
        # If unable to retrieve repositories, exit with an error code
        sys.exit(1)
else:
    # If the provided GitHub URL is invalid, exit with an error code
    sys.exit(1)
