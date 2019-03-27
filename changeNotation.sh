b#!/bin/bash

# usage changeNotation.sh figure rawfigure will change instances of \figure{ to \rawfigure{

list=(ai amazon data-science deepgp dimred gp gplvm gpss health kern ml mlai mlss philosophy privacy supply-chain sysbio uq vision)
for i in ${list[@]}; do
    if [ -d "_${i}/includes/" ]; then
	expression="s/\\\\${1}{/\\\\${2}{/g"
	echo Directory ${i} searching $expression
	sed -i .bak "$expression" _${i}/includes/*.md
    fi
done

list=(talk-macros-back talk-macros-docx talk-macros-front talk-macros-html talk-macros-ipynb talk-macros-notes talk-macros-notes-docx talk-macros-notes-html talk-macros-notes-ipynb talk-macros-notes-tex tal-macros-slides talk-macros-slides.html talk-macros-slides-ipynb talk-macros-slides-tex talk-macros-tex)
for i in ${list[@]}; do
    if [ -f "${i}" ]; then
	expression="s/\\\\${1}{/\\\\${2}{/g"
	echo File ${i} searching $expression
	sed -i .bak "$expression" ${i}
    fi
done
