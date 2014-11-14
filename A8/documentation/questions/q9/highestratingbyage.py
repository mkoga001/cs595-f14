#!/usr/local/bin/python

import sys

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
def getUserDetails(userfile, genderValue, agebarrier, criteria):

    userdict = {}
    print criteria 
    for line in userfile:
        
        line   = line.split("|")         
        uid    = line[0]
        age    = int( line[1] )
        gender = line[2]
        occupation = line[3]
        #Added the below condition for the code which I wrote for question 3
        if criteria == "under":     
            if gender == genderValue and age < agebarrier :
                userdict[ uid ] = occupation
                #userdict.append(uid)
        if criteria == "over":
            if gender == genderValue and age > agebarrier :
                userdict[ uid ] = occupation
                
    #print userdict
    return userdict 
    
if __name__ == '__main__':
    countofTopRatings = int(sys.argv[1])
    criteria = sys.argv[2]
    agebarrier = int(sys.argv[3])
    genderValue = sys.argv[4]
    
    
    ratingsfile = open ("../data/u.data", "r")
    moviesfile  = open ("../data/u.item", "r")
    userfile    = open ("../data/u.user", "r")
    userdetails = getUserDetails(userfile,genderValue,agebarrier,criteria)
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
    movieRatings = []
    
    