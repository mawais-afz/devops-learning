#!/bin/bash  
  
d=`date +%m-%d-%Y`  

echo -e "Date in format DD-MM-YYYY \c: "; d=`date +%d-%m-%Y`
echo $d #DD-MM-YYYY

echo -e "Date in format YYYY-MM-DD \c: "; d=`date +%Y-%m-%d`
echo $d #YYYY-MM-DD

echo -e "Date in format MM/DD/YY \c: "; d=`date +%m/%d/%y`
echo $d #MM/DD/YY

echo -e "Full date with weekday and month name \c: "; d=`date +"%A, %B %d, %Y"`
echo $d #e.g. Monday, January 01, 2024

echo -e "Date with time (24-hour format) \c: "; d=`date +"%Y-%m-%d %H:%M:%S"`
echo $d #YYYY-MM-DD HH:MM:SS

echo -e "Date with time (12-hour format) \c: "; d=`date +"%m/%d/%Y %I:%M:%S %p"`
echo $d #MM/DD/YYYY HH:MM:SS AM/PM