from datetime import datetime
import os
import urllib.request
import re

tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()

print(loglines)

for log in loglines:
    time = datetime.fromtimestamp(log)
    print(time)

