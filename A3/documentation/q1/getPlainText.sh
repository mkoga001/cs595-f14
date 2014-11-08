#!/bin/bash

directory="/home/mkogatam/mallika/cs595/A3/q1/2014-09-27_15.51.01"
rawfiles=`ls $directory`

plainfile="/home/mkogatam/mallika/cs595/A3/q1/2014-09-27_15.51.01-processed"
mkdir $plainfile

for file in $rawfiles
do 
    echo $file
    lynx -dump -force_html "$directory/$file" >> $plainfile/`basename "$file" .raw`.processed
done
    