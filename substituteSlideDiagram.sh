#!/bin/bash

for dir in _*
do
    for file in `find $dir -maxdepth 1 -name '*.md'`		
    do	
	if grep -q "diagramsDir/" $file
	then
	    sed -i-sett -e 's+\.\./\\diagramsDir/+\\writeDiagramsDir/+g' $file
	    sed -i-sett -e 's+'"'"'\\diagramsDir/+'"'"'\\writeDiagramsDir/+g' $file
	    sed -i-sett -e 's+"\\diagramsDir/+"\\writeDiagramsDir/+g' $file
	fi
    done
    if [ -d $dir/includes ]
    then
	for file in `find $dir/includes -maxdepth 1 -name '*.md'`
	do
	    if grep -q "diagramsDir/" $file
	    then
		sed -i-sett -e 's+\.\./\\diagramsDir/+\\writeDiagramsDir/+g' $file
		sed -i-sett -e 's+'"'"'\\diagramsDir/+'"'"'\\writeDiagramsDir/+g' $file
		sed -i-sett -e 's+"\\diagramsDir/+"\\writeDiagramsDir/+g' $file
	    fi
	done
    fi
done
