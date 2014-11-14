#!/usr/local/bin/python

import sys
from itertools import groupby

def getRatings(ratingsfile,userdetails):
    
    itemsdict = {}
    for line in ratingsfile:
        (user_id, item_id, rating, timestamp ) = line.split('\t')
        #items = line.split('\t')
        rating = float(rating)
        if user_id in userdetails: 
            try:
                itemsdict[item_id].append( rating )
            except KeyError:
                itemsdict[item_id] = list()
                itemsdict[item_id].append( rating )
    return itemsdict
    
def getMovieNames(moviesfile):

    movienamesdict = {}
    for line in moviesfile:
        #print line
        line  = line.split("|")         
        id    = line[0]
        title = line[1]
        movienamesdict[ id ] = title
    return movienamesdict
    
def getUserDetails(userfile, genderValue):

    userdict = {}
    for line in userfile:
        #print line
        line   = line.split("|")         
        uid    = line[0]
        age    = line[1]
        gender = line[2]
        
        if gender == genderValue:
            userdict[ uid ] = age
    #print(userdict)
    return userdict     
if __name__ == '__main__':
    countofTopRatings = int(sys.argv[1])
    genderValue = sys.argv[2]
    
    ratingsfile = open ("../data/u.data", "r")
    moviesfile  = open ("../data/u.item", "r")
    userfile    = open ("../data/u.user", "r")
    userdetails = getUserDetails(userfile,genderValue)
    ratings     = getRatings(ratingsfile,userdetails)
    movienames  = getMovieNames(moviesfile)
    movieRatings = []
    
    for movie in ratings:
        movieRatings.append( (
            movienames[ movie ],  sum( ratings[movie] ) / len( ratings[movie] ),
            len( ratings[movie] )            
        ) )
 
    movieRatings.sort(key=lambda rating: rating[1], reverse = True )
 
    for rating in movieRatings[0:countofTopRatings]:
        print "{} {:.2f}".format( *rating )
        
    
       
    
    
    
    
    
    