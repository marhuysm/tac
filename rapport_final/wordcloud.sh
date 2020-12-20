#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR=1974

cat ../data/txt/*_${YEAR}_*.txt > ${YEAR}.txt
python3 wordcloud_filtering.py $YEAR
wordcloud_cli --text ${YEAR}_keywords.txt --imagefile ${YEAR}_wordcloud.png --width 1000 --height 500  --background="white"
#  display ${YEAR}_wordcloud.png
