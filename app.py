from flask import Flask, request, render_template, redirect
from reader import reader

app = Flask(__name__)

posts = reader('posts.txt')

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def home():
    return render_template('index.html', posts=posts)

@app.route('/projects.html')
@app.route('/projects')
def projects():
    return render_template('projects.html', posts=posts)

@app.route('/resume.html')
@app.route('/resume')
def resume():
    return redirect('/static/assets/resume.pdf')

@app.route('/rtlsdr')
def rtl():
    return render_template('projects.html#rtlsdr', posts=posts)

@app.route('/gokart')
def gokart():
    return render_template('projects,html#gokart', posts=posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080")
