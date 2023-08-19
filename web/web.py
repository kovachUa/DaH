from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')



@app.route('/save_repo', methods=['POST'])
def save_repo():
    repo_url = request.form['repo_url']
    subprocess.Popen(['python3', './scrypt/save_repo.py', repo_url])
    return "Script execution started with Repo URL: " + repo_url

@app.route('/site_url', methods=['POST'])
def site_url():
    site_url = request.form['site_url']
    subprocess.Popen(['python3', './scrypt/site_url.py', site_url])
    return "Script execution started with Site URL: " + site_url

if __name__ == '__main__':
    app.run(host='0.0.0.0',port = 5001)
