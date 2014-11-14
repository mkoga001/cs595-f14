#!/usr/local/bin/python

import sys
from itertools import groupby

def getRatings(ratingsfile):
    
    itemsdict = {}
    
    for line in ratingsfile:
        (user_id, item_id, rating, timestamp ) = line.split('\t')
        #items = line.split('\t')
        rating = float(rating)
        
        try:
            itemsdict[item_id].append( rating )
        except KeyError:
            itemsdict[item_id] = list()
            itemsdict[item_id].append( rating )
            
    return itemsdict
    
    
def getnames(moviesfile):

    namesdict = {}
    
    for line in moviesfile:
        #print line
        line  = line.split("|")         
        id    = line[0]
        title = line[1]
        
        namesdict[ id ] = title
    
    return namesdict
        

if __name__ == '__main__':
    countofTopRatings = int(sys.argv[1])
    
    ratingsfile = open("../data/u.data", "r")
    moviesfile  = open ("../data/u.item", "r")
    ratings     = getRatings(ratingsfile)
    names       = getnames(moviesfile)
    
    #print ratings
    
    movieRatings = []
    
    for movie in ratings:
        movieRatings.append( (
            names[ movie ],  sum( ratings[movie] ) / len( ratings[movie] ),
            len( ratings[movie] )            
        ) )
 
    movieRatings.sort(key=lambda rating: rating[2], reverse = True )
 
    for rating in movieRatings[0:countofTopRatings]:
        print "{} {}".format( rating[0], rating[2] )
       
    
    
    
    
    
    