#!/bin/bash
counting_list=(1 2 3 4 5 6 7 8 9 10)
# print value only from 1st index
echo $counting_list # 1

echo ${counting_list[@]}

echo ${counting_list[0]}
