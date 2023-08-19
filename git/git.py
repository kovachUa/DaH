import os
import json
import subprocess
import time

sleep_time = 3600
wait_time = 600

def download_repo(repo_url, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    subprocess.run(["git", "clone", repo_url, target_directory])

def update_repo(repo_directory):
    if os.path.exists(repo_directory):
        os.chdir(repo_directory)
        try:
            subprocess.run(["git", "pull"])
        except subprocess.CalledProcessError as e:
            print(f"Error updating repository '{repo_directory}': {e}")
    else:
        print(f"Error: Repository directory '{repo_directory}' does not exist.")

def process_json_file(json_path, target_root_directory):
    with open(json_path, 'r') as file:
        data = json.load(file)
        repo_urls = data["urls"]

        for repo_url in repo_urls:
            repo_name = repo_url.split("/")[-1].replace(".git", "")
            repo_directory = os.path.join(target_root_directory, repo_name)

            if os.path.exists(repo_directory):
                update_repo(repo_directory)
                try:
                    subprocess.run(["git", "push"], cwd=repo_directory)
                except subprocess.CalledProcessError as e:
                    print(f"Error pushing changes for repository '{repo_directory}': {e}")
            else:
                download_repo(repo_url, repo_directory)

def main():
    json_directory = "/json/git"
    target_root_directory = "/mirror/git"

    while True:
        json_files = [f for f in os.listdir(json_directory) if f.endswith(".json")]

        if json_files:
            for json_file in json_files:
                json_path = os.path.join(json_directory, json_file)
                repo_name = os.path.splitext(json_file)[0]
                repo_directory = os.path.join(target_root_directory, repo_name)
                process_json_file(json_path, repo_directory)
        else:
            print(f"No JSON files found in directory '{json_directory}'. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)

        print("Waiting before the next run...")
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
