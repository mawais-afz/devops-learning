#!/bin/bash  
  

read -p "Enter User type:" user_type  

if [ ${user_type,,} == "admin" ];
then
echo "Welcome Admin"
elif [ ${user_type,,} == "user" ];
then
echo "Welcome User"
else
echo "Invalid User"
fi
