from parser import parse_ast

# Function to generate Java code from the parsed Python AST
def generate_java_code(python_ast):
    if python_ast is None:
        return ""
    
    java_code = []
    
    for node in python_ast.body:
        java_code.append(parse_ast(node))
    
    return "\n".join(java_code)
