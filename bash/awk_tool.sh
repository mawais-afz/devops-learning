#!/bin/bash
# echo one two three four >> file.txt


awk '{print $0}' file.txt

awk '{print $1}' file.txt

awk '{print $2}' file.txt

awk '{print $3}' file.txt

awk '{print $4}' file.txt

awk '{print $1, $2}' file.txt


# Reading from csv file
awk -F ',' '{print $1, $2}' csvfile.csv


# Using Pipeline
echo "Just get the second word: Pakistan" | awk '{print $2}'


echo "Just get the second word: Pakistan" | awk -F ':' '{print $2}' | cut -c 1-9

echo "Just get the second word: Pakistan" | awk -F ':' '{print $2}' | cut -c2

echo "Just get the second word: Pakistan" | awk -F ':' '{print $2}' | cut -c2-