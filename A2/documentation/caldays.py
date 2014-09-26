#!/usr/local/bin/python3

import sys
import time
import datetime

#carbonDate1 = sys.argv[1]

file = open("cDate.txt",'r')

for line in [l.strip() for l in file if l.split()]:

    try:
        #print line.split()
        data = line.split()
        if len(data) != 2:
            print 0, data[0]
            #data = (datetime.now(),data)
        else:
            (cdate, uri) = data
            ct = time.strptime(cdate, "%Y-%m-%dT%H:%M:%S")
            
            cdt = datetime.datetime.fromtimestamp(time.mktime(ct))
            now = datetime.datetime.now()
            days = (now - cdt).days
            print(str(days) + ' ' + uri)
    except ValueError:
        # skip over those items without carbon dates
        print ('0'+ ' ' + uri) 

file.close()