#! /usr/bin/env python

import math

def main():
    idf = math.log(
        float( 1007 ) / 235 ,
        2
    )
    data_rank = open( "pageranks.txt", "r" )
    data_tdif = open( "wrd_uri.txt" ,"r")
    print "{:>8}    {:^12}      {:^37}".format( 
        "Page Rank",
        "TFDIF",
        "URI"
    )
    print "-" * 65
    
    for rank in data_rank:
        rank = rank.split()
        data_tdif = open( "wrd_uri.txt" ,"r")
        for tfidf in data_tdif:
            tfidf = tfidf.split()
            #print line[0:2] + line[3:]
            rank_url  = rank[0]
            page_rank = rank[1]
            tdif_url  = tfidf[3]
            if tdif_url==rank_url: 
                count_word    = float(tfidf[0])
                count_keyword = float(tfidf[1])
                tf    = count_keyword / count_word
                tfidf = tf * idf
                            
                try:
                    page_rank = [ float( x.strip() ) for x in page_rank.split("/") ]
                    page_rank = page_rank[0] / page_rank[1]
                    
                    page_rank = "{:>8.2f}".format( page_rank )
                except ValueError:
                    page_rank = 0
                            
                print "{:>8}    {:>8.2f}    {}".format(
                    page_rank,
                    tfidf,
                    tdif_url
                )
    
if __name__ == "__main__":
    main()