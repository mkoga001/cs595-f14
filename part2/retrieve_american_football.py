#! /usr/bin/env python                          

# Mallika Kogatam	
# Fall 2014
# Assignment 1 part 2

import os
import sys
import urllib2
import time

from bs4 import BeautifulSoup

def main():
	if len( sys.argv ) != 4:
		print "Usage Error"
		sys.exit(0)
	
	#url = "http://sports.yahoo.com/college-football/scoreboard/"
	url = sys.argv[3]
	team = str( sys.argv[1] ).lower()
	
	try:
		sleep_time = int( sys.argv[2] )
	except ValueError:
		print "Time must be an integer"
		sys.exit(1)
		
	html = urllib2.urlopen( url ).read()
	soup = BeautifulSoup(html)
	
	while True:
		score_rows = soup.find_all("tbody")[1].find_all("tr")
		
		for row in score_rows:		
		
			cols = row.find_all("td")
			
			if len( cols )  == 5:
				cols = cols[1:4]
				#print "="*32

				team1 = cols[0].find_all("em")[0].contents[0]			
				team2 = cols[2].find_all("em")[0].contents[0]
				scores =  [score.contents[0] for score in cols[1].find_all("span")]
				
				if team1.lower() == team or team2.lower() == team:
					print team1, scores[0], ",", team2, scores[1]
					
		time.sleep(sleep_time)
					
					

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(1)
		