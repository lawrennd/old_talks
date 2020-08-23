#!/bin/bash


SLIDEDIR=$(../talkfield.py slidedir $1)
echo $SLIDEDIR
for file in $(../dependencies.py slidediagrams $1)
do
    echo "Copying $file to $SLIDEDIR/$file"
    mkdir -p `dirname $SLIDEDIR/$file` && cp $file $SLIDEDIR/$file
done
