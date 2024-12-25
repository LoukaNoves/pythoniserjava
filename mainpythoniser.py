from parser import parse_python_code
from generator import generate_java_code
from compiler import compile_and_run_java_code

def main():
    python_code = """
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 4)
print(result)
"""
    
    # Step 1: Parse the Python code into an AST
    python_ast = parse_python_code(python_code)
    
    # Step 2: Generate Java code from the parsed AST
    java_code = generate_java_code(python_ast)
    
    # Step 3: Compile and run the generated Java code
    compile_and_run_java_code(java_code)

if __name__ == "__main__":
    main()
