#!/usr/local/bin/python3
import re
import sys
import urllib2
import collections 

mementostructure = re.compile(r'rel.*?=.*?"memento".*?')

def getTimeMap(url):
    mem_url = "http://mementoweb.org/timemap/link/" + url
    try:
        response = urllib2.urlopen(mem_url)
        timemap = response.read()
    except urllib2.HTTPError:
        timemap= None
    return timemap
    
def countMementos(mem_url):
    time_map = getTimeMap(mem_url)
    if not time_map:
        count = 0
    else:
        count = len(mementostructure.findall(str(time_map)))
    return count
    
if __name__ == "__main__":
    #inputfile = (sys.argv[2])
    f = open ('listUrlCdate.txt','r')
    memlist = []
    for line in f.readlines():
        mementoCount = countMementos(line.strip())
        memlist.append(mementoCount)
        #print (str(mementoCount), line.strip())
        sys.stdout.flush()
    x=collections.Counter(memlist)
    mementos =(x.most_common())
    for i in mementos: 
        numbers = " ".join(str(x) for x in i) 
        print numbers
    f.close()