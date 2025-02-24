#!/bin/bash

# String Length
str="Hello World"
echo "String length demonstration:"
echo "String: $str"
echo "Length: ${#str}"
echo

# String Concatenation
str1="Hello"
str2="World"
str3=$str1$str2
echo "String concatenation demonstration:"
echo "String 1: $str1"
echo "String 2: $str2"
echo "Concatenated: $str3"
echo

# String Substring
string="Hello World"
echo "Substring demonstration:"
echo "Original string: $string"
echo "Substring (position 1-5): ${string:0:5}"
echo "Substring (from position 6): ${string:6}"
echo

# String Replacement
text="The cat and the other cat"
echo "String replacement demonstration:"
echo "Original text: $text"
echo "Replace first 'cat': ${text/cat/dog}"
echo "Replace all 'cat': ${text//cat/dog}"
echo

# String Case Conversion
sample="Hello World"
echo "Case conversion demonstration:"
echo "Original: $sample"
echo "Uppercase: ${sample^^}"
echo "Lowercase: ${sample,,}"
echo

# String Comparison
str1="hello"
str2="hello"
str3="world"

echo "String comparison demonstration:"
if [ "$str1" == "$str2" ]; then
    echo "'$str1' equals '$str2'"
fi

if [ "$str1" != "$str3" ]; then
    echo "'$str1' is not equal to '$str3'"
fi

# String Empty/Not Empty Check
empty=""
text="Not empty"

echo -e "\nEmpty string check demonstration:"
if [ -z "$empty" ]; then
    echo "String is empty"
fi

if [ -n "$text" ]; then
    echo "String is not empty"
fi

# String Contains Check
string="Hello World"
if [[ $string == *"World"* ]]; then
    echo -e "\n'$string' contains 'World'"
fi

# String Trim
text="   Hello World   "
trimmed=$(echo "$text" | xargs)
echo -e "\nTrim demonstration:"
echo "Original: '$text'"
echo "Trimmed: '$trimmed'"


# String Find/Search
echo -e "\nString find/search demonstration:"
text="The quick brown fox jumps over the lazy dog"
search="fox"

# Method 1: Using grep
echo "Using grep:"
if echo "$text" | grep -q "$search"; then
    position=$(echo "$text" | grep -b -o "$search" | cut -d: -f1)
    echo "Found '$search' in the text at position $position"
fi

# Method 2: Using case statement
echo -e "\nUsing case statement:"
case "$text" in
    *"$search"*) echo "Found '$search' in the text" ;;
    *) echo "'$search' not found" ;;
esac

# Method 3: Using parameter expansion
echo -e "\nUsing parameter expansion:"
if [[ "$text" == *"$search"* ]]; then
    echo "Found '$search' in the text"
fi

# Method 4: Using expr match
echo -e "\nUsing expr match:"
if expr "$text" : ".*$search.*" > /dev/null; then
    echo "Found '$search' in the text"
fi

# Method 5: Using awk
echo -e "\nUsing awk:"
if echo "$text" | awk "/$search/ {print \"Found '$search' in the text\"; exit}" | grep -q .; then
    :
fi

# Method 6: Using sed
echo -e "\nUsing sed:"
if echo "$text" | sed -n "/$search/p" | grep -q .; then
    echo "Found '$search' in the text"
fi

# Method 7: Using bash regex operator =~
echo -e "\nUsing bash regex operator:"
if [[ "$text" =~ $search ]]; then
    echo "Found '$search' in the text"
fi


# String Split
echo -e "\nString split demonstration:"
sentence="apple,banana,orange,grape"
echo "Original string: $sentence"

# Split using IFS (Internal Field Separator)
echo "Split using IFS:"
IFS=',' read -ra fruits <<< "$sentence"
for fruit in "${fruits[@]}"
do
    echo "- $fruit"
done

# Split using tr command
echo -e "\nSplit using tr command:"
echo "$sentence" | tr ',' '\n'

# Split using cut command
echo -e "\nSplit using cut command:"
echo "$sentence" | cut -d',' -f1-4

# Split and process each item
echo -e "\nSplit and process each item:"
for item in ${sentence//,/ }
do
    echo "Processing: $item"
    echo "Length of $item is ${#item} characters"
done
