import json

def add_website_with_rss(data, name, site, rss):
    data["websites_with_rss"].append({"name": name, "site": site, "rss": rss})

def main():
    data = {"websites_with_rss": []}

    while True:
        address = input("Введіть адресу сайту (або введіть 'exit' для завершення): ")
        if address.lower() == "exit":
            break
        name = input("Введіть назву сайту: ")
        rss = input("Введіть адресу RSS для сайту (або натисніть Enter, якщо відсутня): ")
        add_website_with_rss(data, name, address, rss)

    data["websites_with_rss"] = sorted(data["websites_with_rss"], key=lambda x: x["name"].lower())

    with open("site.json", "w") as site_file:
        json.dump(data["websites_with_rss"], site_file, indent=4)

if __name__ == "__main__":
    main()
