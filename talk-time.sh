#!/bin/bash

./mdpp.py $1 -o tmp.markdown --format notes --to html ${PPFLAGS} 
WORDS=`wc -w tmp.markdown | sed -e 's/^[[:space:]]*//' | cut -f1 -d' '`
TIME=$((WORDS/120))
echo "$TIME minutes"
