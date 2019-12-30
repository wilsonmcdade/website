"""
Wilson's file reader lol
"""

def reader(filename):
    posts = []
    file = open(filename)

    for lines in file:
        syntax = lines[:2]
        if syntax == "%e":
            file.close()
            return posts
        elif syntax == "%P":
            posts.append(parser(lines,file,posts))
        else:
            pass
    file.close()
    return posts

def parser(lines,file,posts):
    url = ""
    title = ""
    para = ""
    picsrc = ""
    text = []

    for line in file:
        synt = line[:2]
        rest = line[2:]
        if synt == "%u":
            url = rest.strip()
        elif synt == "%T":
            title = rest.strip()
        elif synt == "%p":
            para = rest.strip()
        elif synt == "%s":
            picsrc = rest.strip()
        elif synt == "%t":
            text.append(rest.strip())
        elif synt == "%P":
            posts.append(parser(lines,file,posts))
    post = {
            'url' : url,
            'title' : title,
            'para' : para,
            'picsrc' : picsrc,
            'text' : text
            }
    return post
