#!/bin/bash

# Basic for loop with a list
echo "1. Basic for loop with a list:"
for name in John Sarah Mike Lisa
do
    echo "Hello, $name!"
done

# For loop with number sequence using {start..end}
echo -e "\n2. For loop with number range:"
for num in {1..5}
do
    echo "Number: $num"
done

# For loop with step value {start..end..step}
echo -e "\n3. For loop with step value:"
for num in {0..10..2}
do
    echo "Even number: $num"
done

# Traditional C-style for loop
echo -e "\n4. C-style for loop:"
for ((i=0; i<5; i++))
do
    echo "Count: $i"
done

# For loop to iterate over files in current directory
echo -e "\n5. Loop through files in current directory:"
for file in *
do
    echo "Found file: $file"
done

# For loop with command substitution
echo -e "\n6. Loop with command output:"
for user in $(cat /etc/passwd | cut -d: -f1)
do
    echo "User: $user"
    # Break after 5 users to keep output manageable
    ((count++))
    if [ $count -eq 5 ]; then
        break
    fi
done
