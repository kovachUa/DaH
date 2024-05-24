from flask import Flask, render_template, request , send_file, send_from_directory
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/save_repo', methods=['POST'])
def save_repo():
    repo_url = request.form['repo_url']
    subprocess.Popen(['python3', './scrypt/git/save_repo.py', repo_url])
    return "Script execution started with Repo URL: " + repo_url

@app.route('/site_url', methods=['POST'])
def site_url():
    site_url = request.form['site_url']
    subprocess.Popen(['python3', './scrypt/httrack/site_url.py', site_url])
    return "Script execution started with Site URL: " + site_url
    
@app.route('/youtube_url', methods=['POST'])
def youtube_url():
    youtube_url = request.form['youtube_url']
    subprocess.Popen(['python3', './scrypt/youtube/youtube_url.py', youtube_url])
    return "Script execution started with YouTube URL: " + youtube_url

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port = 5003)
