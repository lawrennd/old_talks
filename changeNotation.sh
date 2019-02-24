#!/bin/bash

# usage changeNotation.sh figure rawfigure will change instances of \figure{ to \rawfigure{

list=(ai amazon data-science deepgp dimred gp gplvm gpss health kern ml mlai mlss philosophy privacy supply-chain sysbio uq vision)
for i in ${list[@]}; do
    if [ -d "_${i}/includes/" ]; then
	expression="s/\\\\${1}{/\\\\${2}{/g"
	echo Directory ${i} searching $expression
	sed -i .bak "$expression" _${i}/includes/*.md
    fi
done
