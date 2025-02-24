#!/bin/bash
list=(1 2 3 4 5 6 7 8 9 10)

for item in ${list[@]}
do
    echo -n "$item" | wc -c
done
