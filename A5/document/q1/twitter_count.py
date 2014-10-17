#! /usr/bin/env python

import sys


def main():
    file_in = open( "followed-sorted.txt", "r" )
    file_out = open( "twitter.txt", "w" )
    
    counter = 1
    
    for line in file_in:
        line = line.split(" ")
        file_out.write( "{} {}\n".format( counter, line[0] )  )
        counter += 1
        
    file_out.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
        
        