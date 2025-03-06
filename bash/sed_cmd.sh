#!/bin/bash

# 1. Basic substitution
echo -e "1. Basic substitution:"
echo "Hello World" | sed 's/World/Bash/'

# 2. Global substitution (all occurrences in each line)
echo -e "\n2. Global substitution:"
echo "hello hello hello" | sed 's/hello/hi/g'

# 3. Creating a sedtest file for demonstration
cat > sedtest.txt << EOF
The quick brown fox
Jumps over the lazy
Dog while the cat
Watches from afar
EOF

# 4. In-place editing with backup
echo -e "\n3. In-place editing (with backup):"
sed 's/quick/datadog/g' sedtest.txt
echo "Original file backed up as sedtest.txt.bak"
echo "Modified file contents:"
cat sedtest.txt

# 5. Using different delimiters
echo -e "\n4. Using different delimiters:"
echo "/path/to/file" | sed 's:/path:/home:'

# 6. Multiple substitutions
echo -e "\n5. Multiple substitutions:"
echo "hello world" | sed -e 's/hello/hi/' -e 's/world/there/'

# 7. Deleting lines
echo -e "\n6. Deleting specific lines:"
sed '2d' sedtest.txt  # Delete line 2

# 8. Print specific lines
echo -e "\n7. Printing specific lines:"
sed -n '1p' sedtest.txt  # Print only line 1

# 9. Working with line ranges
echo -e "\n8. Working with line ranges:"
sed '2,3s/This/That/' sedtest.txt

# 10. Using regular expressions
echo -e "\n9. Using regular expressions:"
echo "The year is 2023" | sed 's/[0-9]\{4\}/2024/'

# Cleanup
rm sedtest.txt*
echo -e "\nDemo completed!"
