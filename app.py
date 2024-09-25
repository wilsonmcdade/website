from flask import Flask, request, render_template, redirect
from reader import reader
from datetime import datetime
import os, sys
import logging
import random

app = Flask(__name__)
count = 0
posts = reader('posts.txt')

coop = {
    'term' : 'January 2025',
    'type' : 'Computer Science',
    'year' : 'senior'
}

error_text = [
    "Need help finding yourself?",
    "I hope this wasn't my fault. If it was, please let me know!",
    "I hope this wasn't my fault (´･_･`)",
    "Oof"
    ]

footer = {
    'insta' : 'instagram.com/wilsonmcdade',
    'linkedin' : 'linkedin.com/in/wilsonmcdade',
    'email' : 'me@wmcda.de'
    }

tracker = "<script async src=\"https://www.googletagmanager.com/gtag/js?id=G-B8\
H3YC8FGK\"></script><script>window.dataLayer = window.dataLayer || [];function \
gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-B8H3\
YC8FGK');</script>"

@app.route('/projects/<name>')
def post(name):
    for post in posts:
        if post['url'] == name:
            return render_template('post.html',blogpost = post,posts=posts, coop=coop, footer=footer,tracker=tracker)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html', posts=posts, coop = coop, footer=footer, tracker=tracker)

@app.route('/blog')
@app.route('/projects')
@app.route('/drinkr')
@app.route('/rtlsdr')
@app.route('/gokart')
def projects():
    return render_template('blog.html', posts=posts, coop = coop,footer=footer,tracker=tracker)

@app.route('/resume.html')
@app.route('/resume')
def resume():
    return redirect('/static/assets/resume.pdf')

@app.route('/portfolio.html')
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', coop = coop, footer=footer,tracker=tracker)

@app.errorhandler(404)
def error_404(e):
    return render_template('404.html', error_message=error_text[random.randint(0,len(error_text)-1)], coop = coop, footer=footer,tracker=tracker)

if __name__ == "__main__":
    if os.path.exists("logs/") == False:
        os.mkdir("logs/")
    logging.basicConfig(filename='logs/app.log', filemode='a',format='%(asctime)s :: %(levelname)s :: %(message)s')
    logging.info('Begin logging')
    
    app.run("0.0.0.0",port="8080")
