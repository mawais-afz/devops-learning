#!/bin/bash
# Positional parameters
# $1-$9 - positional arguments
# $10-$n - positional agruments after nine
# $0 - name of the script
# $# - total number of agruments
# $$ - PID of the script 

# $0 specifies the name of the script to be invoked.
# $1-$9 stores the names of the first 9 arguments or can be used as the arguments positions.
# $# specifies the total number (count) of arguments passed to the script.
# $* stores all the command line arguments by joining them together.
# $@ stores the list of arguments as an array.
# $? specifies the process ID of the current script.
# $$ specifies the exit status of the last command or the most recent execution process.
# $! shows ID of the last background job.

echo "$1 Welcome to the bash scripting course!"

