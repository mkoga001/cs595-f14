#! /usr/bin/env python

import math

def main():
    data_file = open( "pageranks.txt", "r" )
    
    print "{:>12}    {:^37}".format( 
        "Page Rank",
        "URI"
    )
    print "-" * 45
    
    for line in data_file:
        line = line.split()
        #print line[0:2] + line[3:]
        url       = line[0]
        page_rank = line[1]
        
        try:
            page_rank = [ float( x.strip() ) for x in page_rank.split("/") ]
            page_rank = page_rank[0] / page_rank[1]
            
            page_rank = "{:>8.2f}".format( page_rank )
        except ValueError:
            page_rank = line[1]
                    
        print "{:>12}    {}".format(
            page_rank,
            url
        )
    
    
    
if __name__ == "__main__":
    main()