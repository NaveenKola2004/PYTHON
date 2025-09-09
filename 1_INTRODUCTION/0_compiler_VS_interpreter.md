# Compiler vs Interpreter

## 🔹 Compiler
- Translates the **entire source code** into machine code **at once**.
- Produces a separate **executable file**.
- **Faster execution** after compilation, but initial compilation takes time.
- Errors are shown **after full compilation**.

### Examples:
- C
- C++
- Java (compiles to bytecode)

---

## 🔹 Interpreter
- Translates **line by line** and executes immediately.
- No separate executable is produced.
- **Slower execution**, but good for debugging.
- Errors are shown **immediately**, making it easier to fix.

### Examples:
- Python
- JavaScript
- Ruby

---

## ⚖️ Difference at a Glance

| Feature            | Compiler                           | Interpreter                      |
|---------------------|------------------------------------|-----------------------------------|
| Translation         | Whole program at once             | Line by line                     |
| Output              | Generates an executable file      | No executable file                |
| Speed (Execution)   | Faster (after compilation)        | Slower                           |
| Error Detection     | After compilation (all at once)   | Immediately (line by line)       |
| Examples            | C, C++, Java                      | Python, JavaScript, Ruby         |
