#! /usr/bin/env python

import math

def main():
    idf = math.log(
        float( 1007 ) / 235 ,
        2
    )
    
    #print idf
    
    data_file = open( "wrd_uri.txt", "r" )
    
    print "{:^8} {:^8} {:^8} {:^37}".format( 
        "TFDIF",
        "TF",
        "IDF",
        "URI"
    )
    print "-" * 64
    
    for line in data_file:
        line = line.split()
        #print line[0:2] + line[3:]
        count_word    = float(line[0])
        count_keyword = float(line[1])
        url           = line[3]
        
        tf    = count_keyword / count_word
        tfidf = tf * idf
        
        print "{:>8.2f} {:>8.2f} {:>8.2f} {}".format(
            tfidf,
            tf,
            idf,
            url
        )
    
    
    
if __name__ == "__main__":
    main()