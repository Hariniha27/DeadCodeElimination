# DeadCodeElimination
A Python-based tool that performs Dead Code Elimination (DCE), a compiler optimization technique.
# Dead Code Elimination Tool

## Project Overview
This is a **Dead Code Elimination (DCE) tool** implemented in Python.  
Dead Code Elimination is a compiler optimization technique that **removes code statements that do not affect the program's output**.  
This tool allows users to input Python-like code and outputs an **optimized version** with unused assignments removed.

---

## Features
- Supports **variable assignments** and **print statements**.
- Detects **dead code** (unused variables or assignments) and removes them.
- User-friendly **interactive input**: enter code line by line.
- Prints both **original** and **optimized code**.

---

## Example

### Input:
a = 5

b = 10

c = a + 2

b = b + 5

print(c)

END

### Output:
Original Code:

a = 5

b = 10

c = a + 2

b = b + 5

print(c)

Optimized Code:

a = 5

c = a + 2

print(c)

### Requirements
Python 3.x
No external libraries required.
