#!/bin/bash

links=`cat q2-1-result.txt | cut -f2 -d" "`

for link in $links
do
    file="../q1/2014-09-27_15.51.01-processed/$link"
    hash=`basename $link .processed`
    url=`grep $hash linkmap.txt | cut -d" " -f2` 
    occur=`wc -w $file | cut -d" " -f1`
    words=`grep -ci music $file`
    echo "$occur $words $hash $url"
done 

