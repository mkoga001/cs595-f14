#! /usr/bin/env python                          

# Mallika Kogatam    
# Fall 2014
# Assignment 4 part 1

import os
import sys
import urllib2
import time
import md5

from datetime import datetime

from bs4 import BeautifulSoup

LIMIT = 100

def main():
    
    if len( sys.argv ) != 2:
        print "Usage Error"
        sys.exit(1)
    
    url_filename = sys.argv[1]
    
    try:
        url_file = open(url_filename,"r")
    except IOError:
        print "File {} does not exist".format( url_filename )
        sys.exit(1)
    
    counter = 1
    
    
    
    folder = datetime.now().strftime("%Y-%m-%d.%H.%M.%S")
    
    os.mkdir( folder )
    
    log_file = open( folder + ".log", "w" )
    
    print folder
    
    for url in url_file:

        url = url.strip()
    
        print "%"*40
        print url
        
        url_hash = md5.md5(url).hexdigest()
        
        log_file.write( url_hash + " " + url + "\n" )
        log_file.flush()
        
        try:
            html = urllib2.urlopen( url ).read()
            soup = BeautifulSoup(html)
                
            links = soup.find_all("a")
            
            name = url_hash + ".links"
            link_file = open( "{}/{}".format( folder, name ) ,'w') 
            print "{}/{}".format( folder, name )
            
            for link in links:        
                try:                    
                    
                    href = link["href"]
                    
                    if "http://" in href or "https://" in href:
                        try:
                            link_file.write( href + "\n" )
                            link_file.flush()
                        except UnicodeEncodeError:
                            pass
                    
                except KeyError:
                    pass
            counter += 1
            link_file.close()
            
        except urllib2.HTTPError, urllib2.URLError:
            pass
    
        if counter >= LIMIT:
            break
    
    log_file.close()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
        