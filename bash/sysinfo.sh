#!/bin/bash
# Print username, current data & time, no. of user login


echo "System Information"
echo "------------------"

echo "Hostname: $(hostname)"
echo "Uptime: $(uptime)"
echo "Memory Usage: $(free -h)"
echo "Dist Usage: $(df -h)"


echo "Username: $USER"
echo -e "Current date & time is \c";date
echo -e "User login \c"; who | wc -l
cal
exit 0
