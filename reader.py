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
    url = str
    title = str
    para = str
    picsrc = str
    text = []

    post = {
        'url' : url,
        'title' : title,
        'para' : para,
        'picsrc' : picsrc,
        'text' : text
        }

    for line in file:
        if len(line) > 2:
            synt = line[:2]
            rest = line[2:].strip()
        else:
            print("No attribute. Skipping line.")
            continue

        syntax = {
            "%u":"url",
            "%T":"title",
            "%p":"para",
            "%s":"picsrc",
            "%t":None,
            "%P":None
            }

        if synt in syntax:

            if synt == "%t":
                text.append(rest)
            elif synt == "%P":
                posts.append(parser(lines,file,posts))
            else:
                cmd = syntax[synt]
                post[cmd] = rest

        else:
            print("synt not in syntax")
            pass

    return post
