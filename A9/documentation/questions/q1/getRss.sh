#! /bin/bash

if [ $# -ne 1 ]
then
    echo "Usage: $0 #"
    exit
fi

blogFile=$1 

echo -n "" > `basename $blogFile .txt`-atom.txt

for line in `cat $blogFile`
do
    #curl $line | grep 'rel="alternate"' | grep atom | sed 's/.*href=//' | sed 's/\/>//' | sed 's/"//g' >> `basename $blogFile .txt`-atom.txt


    test=`curl $line | grep 'rel="alternate"' | grep atom | sed 's/.*href=//' | sed 's/\/>//' | sed 's/"//g' | sed 's/ //g'` 
    echo "$test?max-results=1000" >> `basename $blogFile .txt`-atom.txt
done


