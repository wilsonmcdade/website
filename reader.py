"""
Wilson's Config Reader
Built for www.wilsonmcda.de
Author: Wilson McDade / wilsonmcdade@github
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
    blurb = str
    picsrc = str
    text = []

    post = {
        'url' : url,
        'title' : title,
        'blurb' : blurb,
        'picsrc' : picsrc,
        'text' : text
        }

    for line in file:
        if len(line) > 2:
            synt = line[:2]
            rest = line[2:].strip()
        else:
            print("No attribute. Skipping line.")
            print(line)
            continue

        syntax = {
            "%u":"url",
            "%T":"title",
            "%b":"blurb",
            "%s":"picsrc",
            "%c":"code",
            "%t":None,
            "%P":None
            }

        if synt in syntax:

            if synt == "%t":
                text.append(rest)
            elif synt == "%c":
                text.append("</p><pre><code>"+rest+"</code></pre></p>")
            elif synt == "%P":
                posts.append(parser(lines,file,posts))
            else:
                cmd = syntax[synt]
                post[cmd] = rest

        else:
            print("synt not in syntax")
            print(synt,line,syntax)
            pass

    return post
