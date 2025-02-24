#!/bin/bash

# default function
up="before"
since="function"
echo $up
echo $since
showUpTime() {
	local_up=$(uptime -p | cut -c4-)
	local_since=$(uptime -s)
	cat << EOF
--------
This machine has been up for ${local_up}
It has been running since ${local_since}
--------
EOF
}

showUpTime

echo $up
echo $since

showName(){
	echo $1 Welcome to the bash scripting course!
}
showName M.Awais

