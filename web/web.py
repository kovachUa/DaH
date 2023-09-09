from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/revision/', methods=['GET'])
def revision():
    return render_template('revision.html')
    
@app.route('/settings/', methods=['GET'])
def settings():
    return render_template('settings.html')
    
@app.route('/arhiv/', methods=['GET'])
def arhiv():
    return render_template('arhiv.html')

@app.route('/ipfs/', methods=['GET'])
def ipfs():
    return render_template('ipfs.html')
    
@app.route('/torent/', methods=['GET'])
def torent():
    return render_template('torent.html')    

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
    
@app.route('/youtube_url', methods=['POST'])
def youtube_url():
    youtube_url = request.form['youtube_url']
    subprocess.Popen(['python3', './scrypt/youtube_url.py', youtube_url])
    return "Script execution started with YouTube URL: " + youtube_url
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port = 5001)
