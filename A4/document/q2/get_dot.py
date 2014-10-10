#! /usr/bin/env python                          

import os
import sys
def main():

    if len( sys.argv ) != 2:
        print "Usage Error"
        sys.exit(1)
    
    directory_name = sys.argv[1]
    log_filename   = directory_name + ".log"
    print ("digraph dotgraph {")
    #print directory_name
    #print log_filename
    
    log_file = open(log_filename, "r")
    
    table_url_hash = { hash: url for hash, url in [ 
            line.strip().split() for line in log_file
        ]
    }
    
    #print table_url_hash
    
    for root, _ , files in os.walk(directory_name):
        for filename in files:
            links_file = open(os.path.join(root , filename))
            content = links_file.readlines()
            links_file.close()
            
            hash = filename[0:filename.find(".links")]
            
            url = table_url_hash[hash]
            
            for link in content:
                link = link.strip()
                print  '"' +url + '" -> "' + link + '"' + '[label = "' + url + ' links to ' + link + '"];'
   
    print "}"
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)