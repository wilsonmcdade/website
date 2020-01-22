# website
My personal website - wilsonmcdade.com or wilsonmcda.de

This is a flask website built using jinja2 templating with a modified HTML5Up template.

website.py - deals with routing and templating. calls reader() from reader.py

reader.py - deals with interpreting a post file and returning the posts for the website. reader() interprets the beginning of a post file, calls parser() to do the rest of the work.

logger.py - contains logger(), a function called when a route is called that logs the time, route, ip address, and a count of page hits

posts.txt - post file. Contains a list of posts for the website. 

# Post template

%P

%u url or id

%T title of post

%b blurb

%s mainpicture.jpg

%t First paragraph of text

%t Second paragraph of text

%c First block of code

%t Third paragraph of text

You can have as many %t's as you would like. 
