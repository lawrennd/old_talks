#!/bin/bash

# Convert background from https://stackoverflow.com/questions/9155377/set-transparent-background-using-imagemagick-and-commandline-prompt
color=$( convert $1 -format "%[pixel:p{0,0}]" info:- )
convert $1 -alpha off -bordercolor $color -border 1 \
	\( +clone -fuzz 30% -fill none -floodfill +0+0 $color \
       -alpha extract -geometry 200% -blur 0x0.5 \
       -morphology erode square:1 -geometry 50% \) \
       -compose CopyOpacity -composite -shave 1 $2

