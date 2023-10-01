import json
import os
import subprocess
import time

json_file_path = '/json/site.json'
wait_time = 6
sleep_time = 6
def run_backup(url, user_agent, backup_path):
    website = url
    os.makedirs(backup_path, exist_ok=True)
    backup_directory = os.path.join(backup_path, website)
    
    if not os.path.exists(backup_directory):
        subprocess.run(['httrack', website, '--user-agent', user_agent, '-O', backup_path])

while True:
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            
            if 'urls' in data and isinstance(data['urls'], list) and len(data['urls']) > 0:
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0"
                backup_path = '/mirror'
                
                for url in data['urls']:
                    run_backup(url, user_agent, backup_path)
                    
        # Shutting down, waiting and restarting
        time.sleep(sleep_time)
    else:
        time.sleep(wait_time)
