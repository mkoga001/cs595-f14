#!/usr/local/bin/python3
import re
import sys
import urllib2
import collections 
#Regular expression that is used to count the memento from the 
#TimeMap for each link
mementostructure = re.compile(r'rel.*?=.*?"memento".*?')
#Regular expression to find another timemap in the one timemap page.
speciallink = re.compile(r'<.+>;rel=.*?"timemap"')
def getTimeMap(url, prepend=True):
    if prepend:
        mem_url = "http://mementoweb.org/timemap/link/" + url
        #appending the url fro the mementoweb.org in order to get the TimeMap
    else:
        mem_url = url
    try:
        response = urllib2.urlopen(mem_url)
        timemap = response.read()#finding time map for thr url provided
    except urllib2.HTTPError:#if the link gives 404 then make the timemap none
        timemap= None #this way we are not missing the mementos for the links which doesnot have timemap
    return timemap
    
def countMementos(mem_url):
    time_map = getTimeMap(mem_url)
    
    if not time_map:#gives the memento as 0 if the timemap is none
        count = 0
    else:
        
        count = len(mementostructure.findall(str(time_map)))
        special_url = speciallink.findall( str(time_map) )
        
        while len( special_url ) == 1:#checks if there is an another timemap in the existing timemap           
            getlink=re.findall("(<.*?>)",special_url[0].strip())#get the next link by a regular expression
            mem_url = getlink[1][1:-1]#discards the angular tags
            time_map = getTimeMap(mem_url, False)#pass the url to getTimeMap function and do not append to mementoweb
            count += len( mementostructure.findall(str(time_map )) )#appending the new count it to existing count            
            special_url = speciallink.findall( str(time_map) )
            #assigning this link to special_url so that loop continues till the timemaps does not exits
    return count
    
if __name__ == "__main__":
   
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