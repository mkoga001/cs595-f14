#! /bin/bash

echo ""

if [ $# -ne 1 ]
then
    echo "Usage: $0 #"
    exit
fi

num=$1

echo "http://f-measure.blogspot.com/" > blogList-$num.txt 
echo "http://ws-dl.blogspot.com/" >> blogList-$num.txt 

for ((i=0;i< $num;i++))
do 
    curl -I -L 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117' | grep Location | tail -n 1 | cut -d" " -f2 | cut -d"?" -f 1 >> blogList-$num.txt
done
        