# Mission 4 — How programs run

## 1. Task / objective
Run a simple Python program and compare compilers and interpreters.

## 2. Work completed
- Added `hello.py`, which prints `Hello from Python`.
- Kept the existing programming concepts and practice notes.
- Compared when translation happens, typical output, examples and advantages.

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates a program before running it. | Reads and executes instructions at runtime. |
| Typical output | Often produces a separate executable or object code. | Often runs source directly or through an intermediate runtime. |
| One example | C compiler such as `clang`. | Python's interpreter. |
| One advantage | The compiled program can run quickly without translating every instruction each time. | It is convenient to run and debug code interactively. |

A compiler translates a program before that program runs, commonly producing another form of code. An interpreter carries out instructions at runtime. The distinction is useful for understanding how programs are launched, although real language implementations can combine compilation and interpretation. Python's standard runtime compiles source to bytecode and executes it in a virtual machine.

## 3. Commands / tools used
- `python3 mission-04-programs/hello.py` — runs the Python file.
- Python `print()` — displays a line of text.
- VS Code — creates and edits source files.

## 4. My understanding
Source code is a set of instructions. Python runs the file and `print()` sends its message to the terminal. Compiler and interpreter describe different stages of translation and execution; implementations can use both techniques.

## 5. Difficulties faced
The earlier Mission 4 commit contained practice examples but did not include the assignment's required `mission-04-programs/hello.py` file or comparison table.

## 6. How I resolved them
Added the required one-line program and documented the comparison in this mission README.

## 7. Evidence / files
- `hello.py` — required program.
- `practice/` — existing practice examples retained in Git history; their current working-tree deletion state was not changed.
- This README — execution notes and compiler/interpreter comparison.

## 8. Commit details
Original mission commit: `Complete Mission 4 programming concepts and practice`. The required `hello.py` and comparison are recorded as `Complete Mission 4 hello program and comparison`.
