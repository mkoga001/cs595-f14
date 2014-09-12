#! /usr/bin/env python                          

# Mallika Kogatam	
# Fall 2014
# Assignment 1 part 2

import os
import sys
import urllib2
from bs4 import BeautifulSoup

def main():
	url = "http://sports.yahoo.com/college-football/scoreboard/"
	#print url
	
	html = urllib2.urlopen( url ).read()
	#print html
	
	#print "-" * 80
	
	soup = BeautifulSoup(html)
	
	#print soup.prettify().encode("UTF-8")
	
	score_rows = soup.find_all("tbody")[1].find_all("tr")
	
	#for i in range(1,11):
	
	for row in score_rows:		
	
		cols = row.find_all("td")
		
		if len( cols )  == 5:
			cols = cols[1:4]
			print "="*32
			#for col in cols:
			#	print
			#	print col.
			#print cols
			print cols[0].find_all("em")[0].contents[0],
			print "-".join( [score.contents[0] for score in cols[1].find_all("span")] ),
			print cols[2].find_all("em")[0].contents[0]
	
	
	
		
    

if __name__ == "__main__":
     main()