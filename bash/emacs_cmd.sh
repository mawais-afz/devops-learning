#!/bin/bash

# This script demonstrates common Emacs commands and use cases

echo "Common Emacs Commands and Use Cases:"
echo "====================================="

echo "1. Basic Navigation:"
echo "   Ctrl + f : Move forward one character"
echo "   Ctrl + b : Move backward one character" 
echo "   Ctrl + n : Move to next line"
echo "   Ctrl + p : Move to previous line"
echo "   Ctrl + a : Move to beginning of line"
echo "   Ctrl + e : Move to end of line"

echo -e "\n2. Word Navigation:"
echo "   Alt + f  : Move forward one word"
echo "   Alt + b  : Move backward one word"

echo -e "\n3. Screen Navigation:"
echo "   Ctrl + v : Move forward one screen"
echo "   Alt + v  : Move backward one screen"
echo "   Alt + <  : Move to beginning of buffer"
echo "   Alt + >  : Move to end of buffer"

echo -e "\n4. Editing:"
echo "   Ctrl + d : Delete character forward"
echo "   Ctrl + h : Delete character backward"
echo "   Alt + d  : Delete word forward"
echo "   Ctrl + k : Kill (cut) from cursor to end of line"
echo "   Ctrl + y : Yank (paste) last killed text"

echo -e "\n5. Search and Replace:"
echo "   Ctrl + s : Forward incremental search"
echo "   Ctrl + r : Backward incremental search"
echo "   Alt + %  : Query replace"

echo -e "\n6. Files and Buffers:"
echo "   Ctrl + x Ctrl + f : Find file"
echo "   Ctrl + x Ctrl + s : Save file"
echo "   Ctrl + x Ctrl + c : Exit Emacs"
echo "   Ctrl + x b       : Switch buffer"

echo -e "\n7. Windows and Frames:"
echo "   Ctrl + x 2 : Split window horizontally"
echo "   Ctrl + x 3 : Split window vertically"
echo "   Ctrl + x 1 : Keep only current window"
echo "   Ctrl + x o : Switch to other window"

echo -e "\n8. Text Manipulation:"
echo "   Ctrl + Space : Set mark (start selection)"
echo "   Ctrl + w     : Kill (cut) selected region"
echo "   Alt + w      : Copy selected region"
echo "   Ctrl + x u   : Undo"

echo -e "\n9. Help:"
echo "   Ctrl + h t : Tutorial"
echo "   Ctrl + h k : Describe key"
echo "   Ctrl + h f : Describe function"
echo "   Ctrl + h v : Describe variable"

echo -e "\nNote: In terminal-based Emacs, Meta (Alt) key might need to be accessed using ESC"
