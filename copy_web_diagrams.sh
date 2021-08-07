#!/bin/bash

# Copy diagrams to the right subdirectory.
# Takes too arguments, first is the source markdown file, second is either slidediagrams or texdiagrams, third is new directory.
echo Slides Directory: $3

diagrams_dir="../slides/diagrams"

for file in $(dependencies $2 $1)
do
    newfile=${file/$diagrams_dir/$3}
    mkdir -p `dirname $newfile`
    if ! cmp -s $file $newfile ; then
       echo "Copying $file to $newfile"
       cp $file $newfile
    else
	echo "Not copying $file"
    fi
done
