#!/bin/bash

showName(){
	echo $1 Welcome to the bash scripting course!
	if [ "${1,,}" = "Awais" ]; then
		return 0
	else 
		return 1
	fi
}
showName $1
if [ $? = 1 ]; then
	echo "Someone unknown called the function!"
fi	

