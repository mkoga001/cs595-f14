#!/usr/local/bin/python3
import re
import sys
import urllib2
import collections 

mementostructure = re.compile(r'rel.*?=.*?"memento".*?')
speciallink = re.compile(r'<.+>;rel=.*?"timemap"')
def getTimeMap(url, prepend=True):
    if prepend:
        mem_url = "http://mementoweb.org/timemap/link/" + url
    else:
        mem_url = url
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
        special_url = speciallink.findall( str(time_map) )
        
        while len( special_url ) == 1:
            #print special_url[0]
            getlink=re.findall("(<.*?>)",special_url[0].strip())
            mem_url = getlink[1][1:-1]
            #print mem_url
            time_map = getTimeMap(mem_url, False)
            count += len( mementostructure.findall(str(time_map )) )
            #print "-", len(mementostructure.findall(str(time_map )))
            #print time_map
            #print "-", count
            special_url = speciallink.findall( str(time_map) )
            #print special_url
            #momento_rul = extract ()
            #reponse = get
            #momentos     = response.text
    return count
    
if __name__ == "__main__":
    #inputfile = (sys.argv[2])
    f = open ('listUrlCdate.txt','r')
    memlist = []
    for line in f.readlines():
        mementoCount = countMementos(line.strip())   
        memlist.append(mementoCount)
        i = (str(mementoCount), line.strip())
        numbers = "\t".join(str(x) for x in i) 
        print numbers
        sys.stdout.flush()
    
    f.close()