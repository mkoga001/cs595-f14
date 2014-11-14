#!/usr/local/bin/python

import sys
import recommendations 
import operator 

if __name__ == '__main__':
    criteria   = sys.argv[1]
    moviename   = sys.argv[2]
    count       = int(sys.argv[3])
        
    prefs = recommendations1.loadMovieLens('../data')

    output = recommendations1.calculateSimilarItems(prefs, n=1682)
    
    if criteria not in [ "most", "least"]:
        print "Error arg 1 must be either most or least"
        sys.exit(1)
    #print len(ratings)
    
        
    for i in output: 
        print i
    
    
    
        
    
    
    