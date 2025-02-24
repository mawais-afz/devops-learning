#!/bin/bash

# 1. Basic counter until loop
echo "1. Basic counter example:"
i=1
until [ $i -gt 3 ]
do
    echo "Counter: $i"
    ((i++))
done

# 2. C-style until loop
echo -e "\n2. C-style until loop:"
i=0
until ((i >= 5))
do
    echo "Value: $i"
    ((i+=2))
done

# 3. Until loop with break
echo -e "\n3. Until loop with break:"
counter=1
until false
do
    echo "Iteration: $counter"
    if [ $counter -eq 3 ]; then
        break
    fi
    ((counter++))
done

# 4. Reading from a file until EOF
echo -e "\n4. Creating and reading from a file:"
# Create a sample file
cat > temp.txt << EOF
Line 1
Line 2
Line 3
EOF

until ! read -r line
do
    echo "File content: $line"
done < temp.txt

# 5. Until loop with multiple conditions
echo -e "\n5. Multiple conditions:"
x=1
y=5
until [ $x -gt 3 ] || [ $y -lt 3 ]
do
    echo "x=$x, y=$y"
    ((x++))
    ((y--))
done

# 6. Until loop with command execution
echo -e "\n6. Until command execution:"
ping_count=0
until ping -c 1 localhost > /dev/null 2>&1
do
    echo "Waiting for localhost to respond..."
    ((ping_count++))
    if [ $ping_count -eq 3 ]; then
        echo "Max retries reached"
        break
    fi
    sleep 1
done

# 7. Until loop with string comparison
echo -e "\n7. String comparison:"
word="start"
until [ "$word" = "end" ]
do
    echo "Current word: $word"
    if [ "$word" = "start" ]; then
        word="middle"
    elif [ "$word" = "middle" ]; then
        word="end"
    fi
done

# Cleanup
rm temp.txt
