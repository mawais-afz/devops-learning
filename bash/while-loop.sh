#!/bin/bash

# 1. Basic counter while loop
echo "1. Basic counter example:"
i=1
while [ $i -le 3 ]
do
    echo "Counter: $i"
    ((i++))
done

# 2. C-style while loop
echo -e "\n2. C-style while loop:"
i=0
while ((i < 5))
do
    echo "Value: $i"
    ((i+=2))
done

# 3. Infinite loop with break
echo -e "\n3. Infinite loop with break:"
counter=1
while true
do
    echo "Iteration: $counter"
    if [ $counter -eq 3 ]; then
        break
    fi
    ((counter++))
done

# 4. Reading from a file
echo -e "\n4. Creating and reading from a file:"
# Create a sample file
cat > temp.txt << EOF
Line 1
Line 2
Line 3
EOF

while read -r line
do
    echo "File content: $line"
done < temp.txt

# 5. While loop with multiple conditions
echo -e "\n5. Multiple conditions:"
x=1
y=5
while [ $x -le 3 ] && [ $y -ge 3 ]
do
    echo "x=$x, y=$y"
    ((x++))
    ((y--))
done

# Cleanup
rm temp.txt
