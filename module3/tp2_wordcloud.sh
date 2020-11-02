#!/usr/bin/env bash

# Building a wordcloud based on one year of bulletins

YEAR=1929
cat ../data/txt/*_${YEAR}_*.txt > ${YEAR}.txt
python3 tp2_filtering.py $YEAR
wordcloud_cli --text ${YEAR}_keywords.txt --imagefile ${YEAR}.png --width 2000 --height 1000
display ${YEAR}.png
