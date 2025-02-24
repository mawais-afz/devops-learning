#!/bin/bash

echo Do you know bash scripting?
read -p "(Y)es/(N)o? :" answer

case ${answer,,} in
    Y|y|Yes|yes)
        echo "That's amazing."
        echo "Keep learning and growing!"
        echo "You're on the right track!"
        ;;
    N|n|No|no)  
        echo "It's easy. Let's start learning from bash scripting."
        echo "You can begin with the basics and work your way up."
        echo "Keep practicing and you'll get better!"
        ;;
    *)
        echo "Please answer with Yes or No"
        ;;
esac
