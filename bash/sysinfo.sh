#!/bin/bash
# Print username, current data & time, no. of user login


echo "System Information"
echo "------------------"

echo "Hostname: $(hostname)"
echo "Username: $USER"
echo -e "Current date & time is \c: "; date
echo "Uptime: $(uptime)"
echo "Memory Usage: $(free -h)"
echo "Dist Usage: $(df -h)"

cal
exit 0
