#! /usr/bin/env python

from TwitterSearch import *
import unittest
import urllib2
import re
import sys
import socket
import ssl
CONSUMER_KEY = "1QjOMB7IZ00zaTvPmZ6tUrR2R"
CONSUMER_SECRET = "4aolvqxZYw3XwyrzWjiHb6aFAlg7iNodyxmyiIyX8NowefLL53"
OAUTH_TOKEN = "2820592280-iVQDNegTG1CtQLuQ14N9kwIefiVPSTA75zAKeye"
OAUTH_TOKEN_SECRET = "oaUFcXLImxaL0XGUvy3nT1XfBXkVkLNWDmRHkWvvDCozi"

def main():
    tso = TwitterSearchOrder()           # create a TwitterSearchOrder object
    tso.setKeywords(['movies'])            # let's define all words we would like to have a look for
    tso.setLanguage('en')                # we want to see English tweets only
    tso.setCount(100)                    # only give us 100 results per page
    tso.setIncludeEntities(False)        # and don't give us all those entity information
    
    ts = TwitterSearch(
        consumer_key        = CONSUMER_KEY,
        consumer_secret     = CONSUMER_SECRET,
        access_token        = OAUTH_TOKEN,
        access_token_secret = OAUTH_TOKEN_SECRET
    )
    results = 0
    url_list = set()
    counter = 1
    for tweet in ts.searchTweetsIterable(tso): 
    
        try:
            #link = tweet['retweeted_status']['user']['entities']['url']['urls']
            for link in tweet['retweeted_status']['user']['entities']['url']['urls']:
                #Access "expanded_url"
                new_url = link["expanded_url"]
                #print new_url
                url_list.add( new_url )
                
            counter= counter+1
            if counter > 17200:
                break
        except KeyError:
            pass
    processed_urls = []
    for url in set(url_list):
        try:
            response = urllib2.urlopen(url, timeout = 2)
            first = response.geturl()
            #second = urllib2.urlopen(first)
            #print second.geturl()
            #print 'RESPONSE:', response.info()["status"]
            #if "200 OK" in response.info()["status"]:
            #    print response.geturl()
            #    print
            while (url != first):
                url = first
                first = (urllib2.urlopen(first, timeout = 2)).geturl()
            processed_urls.append( first ) 
        except urllib2.HTTPError as e:
            pass
        except urllib2.URLError:
            pass
        except socket.timeout:
            pass
        except ssl.SSLError:
            pass
        except socket.error:
            pass
        except AttributeError:
            pass
    processed_urls = set( processed_urls )
  
  
    for url in processed_urls:
        print url
    
    print len( processed_urls )
   
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
