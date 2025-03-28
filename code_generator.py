def generate_code(function_name):
    """Generates a Python script to execute the function"""
    return f"""
from automation_functions import {function_name}

def main():
    try:
        {function_name}()
        print("{function_name} executed successfully.")
    except Exception as e:
        print(f"Error executing function: {{e}}")

if __name__ == "__main__":
    main()
"""
