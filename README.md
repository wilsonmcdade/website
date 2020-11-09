# Personal Website
Accessible at [wmcda.de](wmcda.de)

This is a Flask website built to run in an OKD container. It's a heavily modified HTML5Up template with blog functionality.

### Local Development

1. Clone the repo
2. Create a virtual environment with
'''
python3 -m venv venv
'''
3. Launch the virtual environment 
'''
source venv/bin/activate
'''
4. Install required files with
'''
pip install -r requirements.txt
'''
5. Run app.py

### Included Files
**app.py** :: Handles routing and initiates the app. The important global variables also live here

**reader.py** :: Parses the posts document and turns it into a 'post' JSON object to be inserted into the template

**posts.txt** :: File containing the posts for the website. There are some built-in tags that are explained below

### Post Templating

**%P** :: Denotes a new post

**%u** :: URL of post

**%T** :: Title of post

**%b** :: Blurb to be seen on the website index

**%s** :: Main picture to be shown on the website index

**%t** :: Paragraph block

**%c** :: Code block
