# advanced_math_calculator.py

import math

def safe_eval(expression):
    """Safely evaluate a mathematical expression with constants and math functions."""
    allowed_names = {
        **math.__dict__,  # Import all math module functions/constants (e.g., sqrt, sin, pi, e)
        "__builtins__": {},  # Disable built-in Python functions for safety
    }

    allowed_chars = "0123456789+-*/%^().// ,"
    if any(char not in allowed_chars for char in expression):
        raise ValueError("Invalid characters in input. Only numbers, math symbols, and supported functions/constants are allowed.")

    # Evaluate the expression in the context of allowed names
    return eval(expression, {"__builtins__": None}, allowed_names)

def calculator():
    print("WELCOME TO MR ALAA'S WORST NIGHTMARE")
    print("HITLER JOKES ARE A MUST")
    print("OTHER THAN THAT WELCOME TO HELL")
    print("THERE IS NO ESCAPE SO DONT EVEN TRY")
    print("NO DUMB FUCKING SHIT CUZ IK U R A DUMBASS")

    while True:
        try:
            # Get the entire mathematical expression
            expression = input("\nEnter your mathematical expression or 'exit': ").strip()
            if expression.lower() == 'exit':
                print("DONT COME BACK")
                break

            # Handle special case for "0 / 0"
            if expression.replace(" ", "") == "0/0":
                print("IF YOU TYPE SOME DUMB SHIT LIKE THAT AGAIN I WILL MURDER YOU")
                continue

            # Safely evaluate the expression
            result = safe_eval(expression)
            print(f"The result is: {result}")
        except ZeroDivisionError:
            print("YA KHARA ANA LESA AYEL NO DUMB SHIT")
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
def correct_addition(a, b):
    if a == 9 and b == 10:
        return 21
    return a + b
result = correct_addition(9, 10)
print("9 + 10 =", result)



if __name__ == "__main__":
    calculator()
