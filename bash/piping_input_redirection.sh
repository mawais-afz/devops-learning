#!/bin/bash

wc -w textfile.txt

wc -w < textfile.txt

cat > textfile.txt << EOF
This is a multi-line
text file created using
heredoc in bash
EOF

wc -w <<< "Hello there word count!"

cat textfile.txt | wc -w