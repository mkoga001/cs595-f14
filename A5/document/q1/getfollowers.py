#! /usr/bin/env python

import tweepy
import time
import sys


CONSUMER_KEY = "1QjOMB7IZ00zaTvPmZ6tUrR2R"
CONSUMER_SECRET = "4aolvqxZYw3XwyrzWjiHb6aFAlg7iNodyxmyiIyX8NowefLL53"
OAUTH_TOKEN = "2820592280-iVQDNegTG1CtQLuQ14N9kwIefiVPSTA75zAKeye"
OAUTH_TOKEN_SECRET = "oaUFcXLImxaL0XGUvy3nT1XfBXkVkLNWDmRHkWvvDCozi"

def main():
    auth = tweepy.auth.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    
    api = tweepy.API(auth)
    
    followed = []
    
    out_file = open( "followed.txt", "w" )
    
    user = api.get_user("phonedude_mln")
    
    
    out_file.write( "{} {}\n".format( user.friends_count, user.screen_name ) )
    
    for friend in user.friends(count = 5000):
        out_file.write( "{} {}\n".format( friend.friends_count, friend.screen_name ) )        
    
    out_file.close()
    
    
   
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
