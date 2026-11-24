# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use Terminal to inspect folders, safely create and manage practice files, explain command options and pipes, and describe package managers.

## 2. Work completed

### Command reference

| Operation | Command | What it does / observation |
|---|---|---|
| Show current directory | `pwd` | Prints the full path of the working folder. |
| List files | `ls` | Shows visible files and directories. |
| Detailed listing | `ls -l` | Adds permissions, owner, size and modification time. |
| Change directory | `cd ..` / `cd folder` | Moves to a parent or named subfolder; `pwd` shows the changed location. |
| Create directory | `mkdir name` | Makes a new folder. |
| Create empty file | `touch file.txt` | Creates an empty file if it does not already exist. |
| Copy file | `cp source copy` | Creates a second file while keeping the source. |
| Move / rename | `mv source destination` | Moves a file or gives it a new name. |
| Display contents | `cat file.txt` | Prints the text in a file. |

### Safe file practice
The `terminal-practice/notes.txt` file contains two lines. The first line was kept when the second was added. `terminal-practice/archive/old-notes.txt` is the renamed backup copy.

- Replacing a file writes new contents over the old contents; appending adds text after the existing contents.
- Copying leaves the original in place. Moving changes the original file's location or name.
- `pwd` tells me which directory relative commands will use. A listing helps me check what is present before acting.

### Flags and pipes
`ls -la` includes hidden entries and detailed metadata; `-h` uses human-readable sizes, for example `ls -lah`. The pipe in `ls -l | head -n 3` sends the listing from the command on the left to `head`, which displays the first three lines.

### Package managers
Homebrew 7.0.9 was already installed. `brew --version` checked its version and `brew list` displayed managed packages. A package manager provides a consistent way to install, update and remove software and can track package dependencies. No software was installed or uninstalled for this activity.

## 3. Commands / tools used
`pwd`, `ls`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `echo`, `ls -la`, `ls -lah`, `head`, the pipe (`|`), `brew --version` and `brew list`.

## 4. My understanding
The current directory determines the context for relative paths. Listing before file operations helps avoid acting on the wrong item. Flags adjust a command and a pipe passes one command's output to another.

## 5. Difficulties faced
The first file listing showed that `notes.txt` had only one line, so the required second-line practice had not yet been saved.

## 6. How I resolved them
Appended a second line to `terminal-practice/notes.txt`, then displayed it and used `wc -l` to confirm that both lines are present.

## 7. Evidence / files
- `terminal-practice/notes.txt` — two-line text practice.
- `terminal-practice/archive/old-notes.txt` — renamed backup copy.
- This README contains the command table and explanations.

## 8. Commit details
Commit: `Mission 2: Terminal practice`. This mission and its documentation are included in the simplified published history.
