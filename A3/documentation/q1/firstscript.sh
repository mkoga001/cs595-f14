#!/bin/bash
links=`cat uniquelinks.txt`

date=`date +"%Y-%m-%d_%H.%M.%S"`

mkdir "$date"

for link in $links
do
    echo $link
    filename=`echo -n $link | md5sum | cut -f1 -d" "`
    echo "$filename $link" >> "$date/linkmap.txt" 
   
    echo $filename
    curl -A "Mozilla/4.0" --connect-timeout 30 "$link" > "$date/$filename.raw"
done
