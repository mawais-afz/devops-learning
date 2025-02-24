
# VIM Tutorial for Beginners

## What is VIM?
VIM (Vi IMproved) is a powerful text editor used in CLI (Command Line Interface). It's an improved version of the vi editor and is highly configurable and efficient.

## VIM Modes
1. **Normal Mode** (Default) - For navigation and manipulation of text
2. **Insert Mode** - For inserting/editing text
3. **Visual Mode** - For selecting blocks of text
4. **Command Mode** - For executing commands

## Basic Commands

### Starting VIM

### Exiting VIM
- `:q`  - Quit (if no changes)
- `:q!` - Force quit (discard changes)
- `:wq` - Save and quit
- `:w`  - Save changes

### Switching to Insert Mode
- `i` - Insert before cursor
- `a` - Insert after cursor
- `o` - Insert new line below
- `O` - Insert new line above

### Navigation (in Normal Mode)
- `h` - Move left
- `j` - Move down
- `k` - Move up
- `l` - Move right
- `w` - Move to next word
- `b` - Move to previous word
- `0` - Move to start of line
- `$` - Move to end of line
- `gg` - Move to start of file
- `G` - Move to end of file

### Text Manipulation
- `dd` - Delete current line
- `yy` - Copy (yank) current line
- `p` - Paste after cursor
- `P` - Paste before cursor
- `u` - Undo
- `Ctrl + r` - Redo

### Search and Replace
- `/pattern` - Search forward for pattern
- `?pattern` - Search backward for pattern
- `n` - Next occurrence
- `N` - Previous occurrence
- `:%s/old/new/g` - Replace all occurrences of 'old' with 'new'

## Practice Exercise
1. Create a new file:
2. 2. Press `i` to enter insert mode
3. Type some text
4. Press `Esc` to return to normal mode
5. Save and quit using `:wq`

## Tips for Beginners
1. Always remember `Esc` returns you to normal mode
2. Use `:help` for built-in documentation
3. Practice basic navigation (hjkl) before advanced commands
4. Create a `.vimrc` file for custom configurations
5. Use `vimtutor` command in terminal for interactive learning

## Common .vimrc Settings
1. `set number` - Show line numbers
2. `set autoindent` - Auto-indent new lines
3. `set tabstop=4` - Set tab width to 4 spaces
4. `set shiftwidth=4` - Set shift width to 4 spaces
5. `set expandtab` - Use spaces instead of tabs
