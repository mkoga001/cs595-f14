#!/usr/local/bin/python

import sys
import recommendations 
import operator 
def getRatings(ratingsfile):
    
    itemsdict = {}

    for line in ratingsfile:
        (user_id, item_id, rating, timestamp) = line.split('\t')
    
        itemsdict.setdefault(user_id,{})
        itemsdict[user_id][item_id] = float(rating)
        
    #print itemsdict
    return itemsdict
    
if __name__ == '__main__':
    
    count       = int(sys.argv[1])
    ratingsfile = open ("../data/u.data", "r")
    ratings     = getRatings(ratingsfile)
    raters      = ratings.keys()
    
    compareraters = {}
    
    for i in range(0,len(raters)):
        bestmatch = recommendations.topMatches(ratings,raters[i],n=len(raters))
                
        if bestmatch[0][1] == raters[i]:
            bestmatch.pop()            
            
        if (bestmatch[0][1],raters[i]) not in compareraters:
            compareraters[(raters[i], bestmatch[0][1])] = bestmatch[0][0]
            
    for item in sorted(
            compareraters, key=compareraters.get, reverse=True
    )[0:count]:
                
        print "{:>4} {:>4} {}".format(
            item[0],
            item[1],
            compareraters[item]
        )
    
    
    
        
    