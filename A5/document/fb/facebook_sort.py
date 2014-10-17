#! /usr/bin/env python

import sys


def main():
    file_in = open( "fb_frnds.txt", "r" )
    file_out = open( "facebook.txt", "w" )
    
    counter = 1
    
    for line in file_in:
        line = line.strip().split(",")
        
        line = [ x.strip() for x in line ]
        
        file_out.write( "{} {}\n".format( line[1], line[0].replace(" ","") ) )
        
        
    file_out.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
        
        