#!/bin/bash

for dir in gpss mlai advds mlphysical execed
do
    cd "$HOME/mlatcl/${dir}"
    git pull
    cd "$HOME/lawrennd/talks/_${dir}"
    ./compile.sh
    cd "$HOME/mlatcl/${dir}"
    git commit -a -m "Recompile slides"
    git push
done
