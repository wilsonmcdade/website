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


if __name__ == "__main__":
    app.run()
