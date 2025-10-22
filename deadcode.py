# dead_code_elimination_user_input.py

def dead_code_elimination(code_lines):
    used_vars = set()
    
    # Step 1: Track used variables (bottom-up)
    for line in reversed(code_lines):
        line = line.strip()
        if line.startswith("print("):
            var = line[6:-1].strip()  # variable inside print
            used_vars.add(var)
        elif "=" in line:
            var, expr = line.split("=", 1)
            var = var.strip()
            expr_vars = [token.strip() for token in expr.replace("+"," ").replace("-"," ")
                         .replace("*"," ").replace("/"," ").split()]
            for ev in expr_vars:
                if ev.isalpha():
                    used_vars.add(ev)

    # Step 2: Build optimized code
    optimized_code = []
    for line in code_lines:
        line = line.strip()
        if "=" in line:
            var, _ = line.split("=", 1)
            var = var.strip()
            if var in used_vars:
                optimized_code.append(line)
                used_vars.remove(var)
        elif line.startswith("print("):
            optimized_code.append(line)

    return optimized_code

# --- User Input ---
if __name__ == "__main__":
    print("Enter your code line by line. Type 'END' (without quotes) to finish:")

    user_code = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        if line.strip():  # ignore empty lines
            user_code.append(line)

    print("\nInput Code:")
    for line in user_code:
        print(line)

    optimized = dead_code_elimination(user_code)

    print("\nOptimized Code:")
    for line in optimized:
        print(line)
