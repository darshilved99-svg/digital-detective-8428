# Mission 02 – Terminal Commands

## Objective
To understand macOS Terminal commands and learn how to navigate, create, read, copy, rename and move files.

## 1. Navigation Commands

| Command | Purpose |
|---|---|
| `pwd` | Displays current directory |
| `ls` | Lists files and folders |
| `cd folder-name` | Enters a folder |
| `cd ..` | Moves to parent directory |

## 2. File and Folder Management

| Command | Purpose |
|---|---|
| `mkdir` | Creates a directory |
| `touch` | Creates an empty file |
| `cat` | Displays file contents |
| `cp` | Copies files |
| `mv` | Moves or renames files |
| `echo` | Writes text to a file |

## 3. Flags and Pipes

- `ls -l`: Displays detailed file information.
- `ls -lh`: Displays file sizes in human-readable format.
- `ls -la`: Displays hidden files and detailed information.
- `ls -l | head -n 3`: Displays the first three lines of command output.

## 4. Practical Activity

Created a folder named `terminal-practice`.

Inside it:
- Created `notes.txt`.
- Added text using `echo`.
- Read the file using `cat`.
- Copied the file using `cp`.
- Renamed the copy using `mv`.
- Created an `archive` folder.
- Moved the renamed file into `archive`.

## 5. Homebrew Exploration

Checked Homebrew using:
- `brew --version`
- `brew list`

Homebrew was installed successfully.

Some installed packages included Git, FFmpeg, Ruby, OpenSSL, Cowsay and Lolcat.

## 6. What I Learned

- Navigating directories using Terminal.
- Creating and managing files and folders.
- Understanding command flags.
- Using pipes to combine commands.
- Exploring installed packages using Homebrew.

## Conclusion

I learned how to use macOS Terminal to manage files and directories and explored Homebrew as a package manager.
