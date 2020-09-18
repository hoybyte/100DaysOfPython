from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    import re
    x = re.search('(\d{4})-(\d{2})-(\d{2})T(\d{2})\:(\d{2})\:(\d{2})', line).group(0)
    return datetime.strptime(x, '%Y-%m-%dT%H:%M:%s')
    pass


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    x = [line for line in loglines if re.search(pattern = SHUTDOWN_EVENT, string = line)]
    first = x[0]
    last = x[-1]
    first_datetime = convert_to_datetime(first)
    last_datetime = convert_to_datetime(last)
    return (last_datetime - first_datetime)
    pass