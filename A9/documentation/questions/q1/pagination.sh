#! /bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 #"
    exit
fi

blogFile=$1 

echo -n "" > `basename $blogFile .txt`-rss.txt

for line in `cat $blogFile`
do
    curl $line | grep 'rel="alternate"' | grep rss | sed 's/.*href=//' | sed 's/\/>//' | sed 's/"//g' >> `basename $blogFile .txt`-rss.txt
done


