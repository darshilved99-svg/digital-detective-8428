# Mission 03 – Operating Systems

## Objective
To understand operating systems, their functions, processes, memory management, file systems, shells and permissions.

## 1. What is an Operating System?

An Operating System (OS) is system software that manages computer hardware and software resources and provides an environment for applications to run.

Examples:
- macOS
- Windows
- Linux
- Android
- iOS

## 2. Types of Operating Systems

- Desktop OS: Used on personal computers.
- Mobile OS: Used on smartphones and tablets.
- Server OS: Manages server resources and services.
- Real-Time OS (RTOS): Provides predictable response times.

## 3. Processes and Threads

**Process:** A program that is currently running.

**Thread:** A unit of execution within a process.

A process can contain multiple threads.

## 4. Memory Management

- RAM: Temporarily stores data used by active applications.
- Virtual Memory: Helps manage memory by using storage when needed.
- Cache: Stores frequently accessed data for faster retrieval.

## 5. File Systems

A file system organizes and manages files on storage devices.

Common file systems:
- APFS – Modern macOS
- NTFS – Windows
- FAT32 – USB drives
- exFAT – Cross-platform storage
- ext4 – Linux

## 6. Shell and Environment Variables

A shell allows users to interact with the operating system through commands.

Common shells:
- Bash
- Zsh
- Fish
- PowerShell

Environment variables:
- PATH – Directories searched for executable commands.
- HOME – User's home directory.
- USER – Current username.

## 7. File Permissions

Three basic permissions:
- Read (r): View file contents.
- Write (w): Modify file contents.
- Execute (x): Run a file as a program.

The `ls -l` command displays file permissions.

## 8. Practical Activity – My Mac

| Component | My System |
|---|---|
| Operating System | macOS 27.2.1 |
| Shell | Zsh |
| Username | darshilvedmutha |
| Home Directory | /Users/darshilvedmutha |
| File System | APFS |
| Disk Capacity | 994.6 GB |
| Available Container Space | 841.4 GB |
| Total Processes | 792 |
| Total Threads | 4,662 |
| CPU Idle | 84.90% |

### Commands Used

- `echo $SHELL` – Checks the current shell.
- `echo $HOME` – Displays the home directory.
- `echo $USER` – Displays the username.
- `diskutil info /` – Displays disk and file system information.
- `top -l 1 | head -n 12` – Displays a snapshot of system activity.
- `ls -l` – Displays file permissions.

## 9. What I Learned

- The role and types of operating systems.
- The difference between processes and threads.
- Memory management concepts.
- File systems and directory structures.
- Shells and environment variables.
- File permissions and system monitoring.

## Conclusion

I learned how operating systems manage computer resources and explored macOS system information using Terminal commands.
