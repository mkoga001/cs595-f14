#!/usr/local/bin/python
import sys
import recommendations1

if __name__ == '__main__':
    
    criteria   = sys.argv[1]
    moviename   = sys.argv[2]
    count       = int(sys.argv[3])
    
    if criteria not in [ "most", "least"]:
        print "Error arg 1 must be either most or least"
        sys.exit(1)
   
   
    prefs = recommendations1.loadMovieLens('../data')
    itemPrefs = recommendations1.transformPrefs(prefs)
    results   = recommendations1.topMatches(itemPrefs,moviename,2000)
    
    if criteria == "most":
        for i in results[0:count]:
            #print i
            print i[0],i[1]
        
    
    if criteria == "least":
    
        results.reverse()
        for i in results[0:count]:
            #print i[0],i[1]
            print i
        

