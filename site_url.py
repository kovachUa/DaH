import os
import json
import sys

def add_website(data, site):
    if "urls" not in data:
        data["urls"] = []
    data["urls"].append(site)

def main():
    if len(sys.argv) != 2:
        return

    website_address = sys.argv[1]
    site_file_path = "/json/site/site.json"

    try:
     
        with open(site_file_path, "r") as site_file:
            data = json.load(site_file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"urls": []}

    add_website(data, website_address)
    
    with open(site_file_path, "w") as site_file:
        json.dump(data, site_file, indent=4)

if __name__ == "__main__":
    main()
