# Mission 3 — Understand the operating system

## 1. Task / objective
Explore operating-system details, processes, storage, paths and file permissions, and explain the OS responsibilities.

## 2. Work completed

### System observations

| Information | What it tells me | Privacy-safe observation |
|---|---|---|
| Operating system | Identifies the OS environment and version. | macOS 27.2.1; shell: Zsh. |
| Current account | Identifies the account running a command. | Checked locally; account name omitted. |
| Available storage | Shows filesystem capacity and remaining space. | Root filesystem: 926 GiB total, 778 GiB available at the time of the check. |
| System activity | Gives a snapshot of running processes and resource use. | Activity Monitor showed 553 processes and 4,457 threads during the observed session; counts can change. |

### Processes
A process is a running program or service. A PID is the number the operating system assigns to a process while it runs. Activity Monitor showed the `Activity Monitor` application (PID 31087 at the time) and system/background processes such as `accountsd`. PIDs and process counts can change between observations.

### Paths and permissions
An absolute path starts from the filesystem root. A relative path is interpreted from the current directory. For example, an anonymized absolute path is `/Users/[redacted]/Downloads/digital-detective-8428/terminal-practice/notes.txt`; the relative path from the repository root is `terminal-practice/notes.txt`.

The detailed listing for `terminal-practice/notes.txt` showed owner permissions `rw-`: the owner can read and write the file but cannot execute it.

| Permission | Meaning | Example |
|---|---|---|
| `r` — read | Allows file contents to be viewed. | Open a text file. |
| `w` — write | Allows a file to be changed. | Edit a text file. |
| `x` — execute | Allows a file to run; on a directory it allows traversal. | Run a script or enter a directory. |

### Operating-system responsibilities

| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts, schedules and monitors running programs. | Activity Monitor lists processes. |
| Memory management | Assigns working memory to programs and reuses it as needed. | A browser uses RAM for open tabs. |
| Device management | Coordinates input/output devices through system software. | macOS routes keyboard input to an application. |
| File management | Organizes files and controls access to them. | A folder groups related project files. |
| User interface / shell | Lets a person interact with the computer. | Zsh accepts Terminal commands. |
| Security and permissions | Controls which users and programs can access resources. | File permission bits restrict writing. |

## 3. Commands / tools used
- `sw_vers` — checked the macOS version.
- `echo $SHELL` — checked the active shell.
- `df -h /` — checked filesystem capacity and available space.
- `pwd`, `cd` and `ls -l` — inspected location and file permissions.
- Activity Monitor — inspected process names and PIDs.
- `top`, `ps` and `diskutil info /` were attempted once; system restrictions prevented those commands from returning results in this environment.

## 4. My understanding
The OS coordinates hardware, programs, memory, files and user access. A process is one active program instance, while its PID identifies it in the current session. Absolute paths do not depend on the current directory; relative paths do.

## 5. Difficulties faced
Terminal access to `top`, `ps` and the DiskManagement framework was restricted.

## 6. How I resolved them
Used Activity Monitor for a process snapshot and `df -h /` for storage. The account name and machine-specific identifiers are omitted from this public note.

## 7. Evidence / files
- This README records the privacy-safe system observations, permissions and OS responsibilities.
- `terminal-practice/notes.txt` is the file whose permissions were inspected.

## 8. Commit details
Original mission commit: `Complete Mission 3 operating systems`. The privacy-safe observations and required tables are recorded as `Document operating-system observations and permissions`.
