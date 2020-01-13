"""
Wilson's logger
"""

def logger(route, ip, file, count):
    count += 1
    log = str(str(count)+" : "+str(ip)+": "+route+"\n")
    file.write(log)
    file.flush()
    return count
