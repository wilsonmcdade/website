from flask import Flask, request, render_template, redirect
from reader import reader
from logger import logger
from datetime import datetime
import os, sys
import random

app = Flask(__name__)
count = 0
posts = reader('posts.txt')

coop = {
    'term' : 'Spring 2021',
    'type' : 'Computer Science'
}

error_text = [
    "Need help finding yourself?",
    "I hope this wasn't my fault. If it was, please let me know!",
    "I hope this wasn't my fault (´･_･`)",
    "Oof that sucks",
    "404s suck, don't they"
    ]

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    global count
    count = logger('index', request.environ['REMOTE_ADDR'], file, count)
    return render_template('index.html', posts=posts, coop = coop)

@app.route('/projects.html')
@app.route('/projects')
@app.route('/rtlsdr')
@app.route('/gokart')
def projects():
    global count
    count = logger('projects', request.environ['REMOTE_ADDR'], file, count)
    return render_template('projects.html', posts=posts, coop = coop)

@app.route('/resume.html')
@app.route('/resume')
def resume():
    global count
    count = logger('resume', request.environ['REMOTE_ADDR'], file, count)
    return redirect('/static/assets/resume.pdf')

@app.route('/store.html')
@app.route('/store')
def store():
    global count
    count = logger('store', request.environ['REMOTE_ADDR'],file,count)
    return redirect('https://www.ArtPal.com/wilsonmcdade?r=169782')

@app.route('/portfolio.html')
@app.route('/portfolio')
def portfolio():
    global count
    count = logger('portfolio', request.environ['REMOTE_ADDR'], file, count)
    return render_template('portfolio.html', coop = coop)

@app.errorhandler(404)
def error_404(e):
    global count
    count = logger('404', request.environ['REMOTE_ADDR'], file, count)
    return render_template('404.html', error_message=error_text[random.randint(0,len(error_text)-1)], coop = coop)

if __name__ == "__main__":
    now = datetime.now()
    current_date = now.strftime("%m-%d-%Y")
    current_time = now.strftime("%H-%M-%S")
    filename = "logs/"+str(current_date)+"/"+str(current_time)+".txt"
    if os.path.exists("logs/") == False:
        os.mkdir("logs/")
    if os.path.exists(filename[:16]) == False:
        os.mkdir(filename[:16])
    with open(filename, "a+") as file:
        file.write("Log begin \n")
        file.write(str(current_date)+" - "+str(current_time)+"\n")
        app.run("0.0.0.0",port="8080")
