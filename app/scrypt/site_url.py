import json
import sys

def add_website(data, site):
    data["url"].append(site)

def main():
    if len(sys.argv) != 2:
        return

    website_address = sys.argv[1]

    try:
        with open("site.json", "r") as site_file:
            data = json.load(site_file)
    except FileNotFoundError:
        data = {"url": []}

    add_website(data, website_address)

    with open("site.json", "w") as site_file:
        json.dump(data, site_file, indent=4)

if __name__ == "__main__":
    main()
