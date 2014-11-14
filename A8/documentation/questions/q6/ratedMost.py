#!/usr/local/bin/python

import sys

def getRatings(ratingsfile):
    
    itemsdict = []
    
    for line in ratingsfile:
        (user_id, item_id, rating, timestamp ) = line.split('\t')
        #items = line.split('\t')
        rating = float(rating)
        itemsdict.append( user_id )
        
    #print (itemsdict)        
    return itemsdict
    
if __name__ == '__main__':
    countofTopRatings = int(sys.argv[1])
    
    ratingsfile = open("../data/u.data", "r")
    ratings     = getRatings(ratingsfile)
    
    rating =  set(ratings )
    usercount = []
    
    for user in rating:
        usercount.append( ( user, ratings.count( user ) ) )
     
    usercount.sort(key=lambda rating: rating[1], reverse = True )
    
    for i in usercount[0:countofTopRatings]:
        print str(i[0]) + "  " + str(i[1])
    
    
    