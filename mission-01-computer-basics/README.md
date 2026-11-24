# Mission 1 — Know your computer

## 1. Task / objective
Explain the IPOS cycle, classify hardware and software, and give examples of computer-based systems.

## 2. Work completed

### IPOS example: searching for information online

| Stage | What happens | Hardware / component |
|---|---|---|
| Input | I enter a search query and submit it. | Keyboard or trackpad |
| Processing | The browser and remote search service interpret the query and find matches. | CPU, memory and network hardware |
| Output | Search results appear in the browser. | Display |
| Storage | Browser files or saved history may be written to storage, depending on settings. | SSD |

The query moves from the keyboard to the computer for processing, travels over the network to the search service, and the returned results are displayed. Storage is used only when data such as browser history or cached files is saved.

### Hardware and software I use

| Item | Classification | Software type | Purpose |
|---|---|---|---|
| CPU | Hardware | — | Executes instructions |
| RAM | Hardware | — | Holds data currently in use |
| SSD | Hardware | — | Keeps files and applications when power is off |
| Keyboard | Hardware | — | Enters text and commands |
| macOS | Software | Operating system | Manages hardware and runs applications |
| Python 3 | Software | Application / language runtime | Runs Python programs |
| Visual Studio Code | Software | Application | Edits project files and code |
| Homebrew | Software | Utility | Manages supported command-line packages |

### Other computer systems

| System | Main purpose | Input | Output |
|---|---|---|---|
| ATM | Provides banking services | Card and keypad selection | Cash or account information |
| Smart TV | Plays broadcast or streamed media | Remote control | Picture and sound |
| Ticket kiosk | Sells or prints tickets | Destination and payment selection | Printed or digital ticket |

### System explored
The earlier computer exploration recorded a MacBook Pro with an Apple M5 processor and 16 GB RAM. The current Terminal checks confirmed macOS 27.2.1; hardware details above are kept at the level already recorded in this project.

## 3. Commands / tools used
- `sw_vers` — displays the macOS version.
- `sysctl -n machdep.cpu.brand_string` and `system_profiler SPHardwareDataType` — inspect processor and hardware details.
- `df -h /` — displays filesystem usage and available storage.
- Terminal and system settings — tools for observing the computer.

## 4. My understanding
IPOS describes a useful path for information through a computer. Hardware is the physical equipment; software is the instructions that make it useful. A computer-based system combines inputs, processing and outputs to perform a focused task.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- This README contains the IPOS, hardware/software and everyday-system tables.

## 8. Commit details
Commit: `Mission 1: Computer basics`. This mission and its documentation are included in the simplified published history.
