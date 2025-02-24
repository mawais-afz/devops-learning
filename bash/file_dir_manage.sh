#!/bin/bash

# File and Directory Management Commands Demo

echo "=== File and Directory Management Demo ==="

# 1. Creating Directories
echo -e "\n1. Creating Directories:"
mkdir test_directory
mkdir -p nested/directory/structure  # -p creates parent directories if they don't exist

# 2. Creating Files
echo -e "\n2. Creating Files:"
touch test_file.txt
echo "Hello World" > hello.txt
cat > sample.txt << EOF
This is a multi-line
text file created using
heredoc in bash
EOF

# 3. Copying Files and Directories
echo -e "\n3. Copying Files:"
cp hello.txt hello_backup.txt
cp -r test_directory backup_directory  # -r for recursive copy of directories

# 4. Moving/Renaming Files and Directories
echo -e "\n4. Moving and Renaming:"
mv hello.txt new_hello.txt
mv test_directory new_directory

# 5. Removing Files and Directories
echo -e "\n5. Removing Files and Directories:"
rm sample.txt
rm -i hello_backup.txt  # -i for interactive deletion
rm -r backup_directory  # -r for recursive deletion
rmdir empty_directory   # only works on empty directories

# 6. File Permissions
echo -e "\n6. Changing File Permissions:"
touch permission_file.txt
chmod 755 permission_file.txt  # rwx for owner, rx for group and others
chmod u+x permission_file.txt  # make executable for user

# 7. Listing Files and Directories
echo -e "\n7. Listing Files and Directories:"
ls
ls -l    # detailed listing
ls -la   # include hidden files
ls -lh   # human-readable file sizes

# 8. Finding Files
echo -e "\n8. Finding Files:"
find . -name "*.txt"    # find all .txt files in current directory and subdirectories
find . -type d         # find all directories
find . -type f -size +1M  # find files larger than 1MB

# 9. Checking File/Directory Status
echo -e "\n9. File Status:"
file permission_file.txt
stat permission_file.txt

# 10. Creating and Following Symbolic Links
echo -e "\n10. Symbolic Links:"
ln -s new_hello.txt link_to_hello
readlink link_to_hello

# Cleanup
echo -e "\nCleaning up demo files..."
rm -rf new_directory nested permission_file.txt new_hello.txt link_to_hello

echo -e "\nDemo completed!"
