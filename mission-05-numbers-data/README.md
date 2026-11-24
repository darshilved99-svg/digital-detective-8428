# Mission 5 — Numbers and data

## 1. Task / objective
Convert values among decimal, binary and hexadecimal; verify calculations with Python; build a decimal converter; and explain text encoding.

## 2. Work completed

### 5.1 Manual conversions

| Question | Working and answer |
|---|---|
| Decimal 13 to binary | Divide by 2: remainders from last to first are 1, 1, 0, 1. Therefore `13₁₀ = 1101₂`. |
| Decimal 25 to binary | Divide by 2: remainders from last to first are 1, 1, 0, 0, 1. Therefore `25₁₀ = 11001₂`. |
| Binary 1010 to decimal | `1×2³ + 0×2² + 1×2¹ + 0×2⁰ = 8 + 2 = 10`. |
| Binary 1101 to decimal | `1×2³ + 1×2² + 0×2¹ + 1×2⁰ = 8 + 4 + 1 = 13`. |
| Hexadecimal A to decimal | `A` is 10 in base 16, so the answer is 10. |
| Hexadecimal 1F to decimal | `1×16¹ + 15×16⁰ = 16 + 15 = 31`. |
| Binary 1111 to hexadecimal | `1111₂ = 15₁₀`; 15 is `F` in hexadecimal. |

### 5.2 Python verification

| Expression | Result | Matches manual work? |
|---|---:|---|
| `bin(13)` | `'0b1101'` | Yes |
| `bin(25)` | `'0b11001'` | Yes |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))` | `'0xf'` | Yes; `F` in uppercase |

### 5.3 Converter program
`number_converter.py` asks for a positive whole number and displays its binary and uppercase hexadecimal digits. `bin()` and `hex()` return base prefixes (`0b` and `0x`); slicing off the first two characters leaves the digits. The program handles non-integer and non-positive input with a short message.

| Test number | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | `1101` | `D` |
| 25 | `11001` | `19` |
| 42 | `101010` | `2A` |

### 5.4 Text encoding
- ASCII decimal code for uppercase `A`: 65.
- ASCII decimal code for lowercase `a`: 97.
- An encoding standard maps characters to numbers so a computer can store, send and interpret text consistently. UTF-8 supports many characters beyond basic ASCII; for example, `€` is not part of basic ASCII.
- A bit stores 0 or 1; eight bits make one byte.

## 3. Commands / tools used
- `python3` — runs the program and interactive checks.
- `input()` — reads the entered number; `int()` converts it to a whole number.
- `bin()` — converts a non-negative integer to a binary string.
- `hex()` — converts a non-negative integer to a hexadecimal string.
- Python `ord()` — checks a character's Unicode code point; ASCII characters keep the same numeric values in Unicode.

## 4. My understanding
The base tells how place values are weighted: powers of 10, 2 or 16. Python's conversion functions provide a useful check on manual place-value calculations. Text also needs a shared encoding so the same stored bytes can be interpreted as the intended characters.

## 5. Difficulties faced
The starting converter displayed binary only and raised an error for invalid input; it did not show hexadecimal output or guide the user when input was not a positive integer.

## 6. How I resolved them
Added hexadecimal output and simple checks for non-integer and non-positive input. Ran the required positive test values and an invalid-input check.

## 7. Evidence / files
- `number_converter.py` — working converter.
- This README — manual working, Python checks, three output examples and encoding notes.
- `evidence/mission-05-converter-output.txt` — selected program output from actual runs.

## 8. Commit details
Planned message: `Build number converter and practise data representation`. Push status is recorded after the GitHub push is attempted and verified.
