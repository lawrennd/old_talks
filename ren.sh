#!/bin/bash

list=(ai gp gpss ml kern data-science)
for i in ${list[@]}; do
    for j in ${list[@]}; do
	echo "s/\/${j}\//\/_${j}\//g"
	sed -i .bak "s/\/${j}\//\/_${j}\//g" _${i}/includes/*.html
	sed -i .bak "s/\/${j}\//\/_${j}\//g" _${i}/diagrams/*.html
	sed -i .bak "s/\/${j}\//\/_${j}\//g" _${i}/includes/*.md
	sed -i .bak "s/\/${j}\//\/_${j}\//g" _${i}/diagrams/*.md
    done
done
