#/bin/bash

FILES=""
SKIP=true
while read stub; do
    if $SKIP; then
	SKIP=false
    else
	maketalk $stub
    fi
done < datasets.csv
