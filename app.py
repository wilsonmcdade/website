from flask import Flask, request, render_template, redirect
from reader import reader
from logger import logger
from datetime import datetime
import os, sys

app = Flask(__name__)
count = 0
posts = reader('posts.txt')

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    global count
    count = logger('index', request.environ['REMOTE_ADDR'], file, count)
    return render_template('index.html', posts=posts)

@app.route('/projects.html')
@app.route('/projects')
@app.route('/rtlsdr')
@app.route('/gokart')
def projects():
    global count
    count = logger('projects', request.environ['REMOTE_ADDR'], file, count)
    return render_template('projects.html', posts=posts)

@app.route('/resume.html')
@app.route('/resume')
def resume():
    global count
    count = logger('resume', request.environ['REMOTE_ADDR'], file, count)
    return redirect('/static/assets/resume.pdf')

if __name__ == "__main__":
    now = datetime.now()
    current_date = now.strftime("%m-%d-%Y")
    current_time = now.strftime("%H-%M-%S")
    filename = "logs/"+str(current_date)+"/"+str(current_time)+".txt"
    if os.path.exists(filename[:16]) == False:
        os.mkdir(filename[:16])
    with open(filename, "a+") as file:
        file.write("Log begin \n")
        file.write(str(current_date)+" - "+str(current_time)+"\n")
        app.run("0.0.0.0",port="8080")
