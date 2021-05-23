#!/bin/bash


SLIDEDIR=$(mdfield slidedir $1)
echo Slides Directory: $SLIDEDIR

diagrams_dir="../slides/diagrams"

for file in $(dependencies slidediagrams $1)
do
    newfile=${file/$diagrams_dir/$SLIDEDIR}
    mkdir -p `dirname $newfile`
    if ! cmp -s $file $newfile ; then
       echo "Copying $file to $newfile"
       cp $file $newfile
    else
	echo "Not copying $file"
    fi
done
