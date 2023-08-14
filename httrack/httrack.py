import json
import os
import subprocess
import time

# loading the contents of a json file
with open('/json/site/site.json', 'r') as file:
    data = json.load(file)

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"

# iterating through the list of site URLs
for url in data['urls']:
    # path to the backup directory for the website
    backup_path = '/mirror/site'

    # getting the website URL
    website = url

    # create the backup directory if it doesn't exist
    os.makedirs(backup_path, exist_ok=True)

    # Check if the backup already exists
    if not os.path.exists(os.path.join(backup_path, website)):
        # use httrack command to create a backup of the website
        subprocess.run(['httrack', website, '--user-agent', user_agent, '-O', backup_path])
