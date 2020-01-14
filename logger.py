"""
Wilson's logger
"""

from datetime import datetime

def logger(route, ip, file, count):
    count += 1
    now = datetime.now()
    log_time = now.strftime("%m-%d-%H-%M-%s")
    log = str(str(log_time)+" : "+str(count)+" : "+str(ip)+": "+route+"\n")
    file.write(log)
    file.flush()
    return count
