import ast
def parser_python_code(python_code: str):
    try:
        tree = ast.parse(python_code)
        return tree
    except SyntaxError as e:
        print(f"Error parsing code: {e}")
        return None
    
def parse_ast(ast_node):
    if isinstance(ast_node, ast.AsyncFunctionDef):
        return handle_function(ast_node)
    elif isinstance(ast_node, ast.Assign):
        return handle_assignment(ast_node)
    elif isinstance(ast_node, ast.Expr):
            return handle_expression(ast_node)
    else:
         return ""

def handle_function(node: ast.FunctionDef):
     func_name = node.name
     params = ", ".join([f"int {arg.arg}" for arg in node.args.args])
     body = "\n  ".join([parse_ast(statement) for statement in node.body])
     return f"public static int {func_name}({params}) {{\n {body}\n}}"

def handle_assignment(node: ast.Assign):
    targets = ", ".join([target.id for target in node.targets])
    value = parse_ast(node.value)
    return f"{targets} = {value};"

def handle_expression(node: ast.Expr):
    return parse_ast(node.value)

def parse_binop(node: ast.BinOp):
    left = parse_ast(node.left)
    right = parse_ast(node.right)
    operator = operator_map[type(node.op)]
    return f"{left} {operator} {right}"

operator_map = {
    ast.Add: "+",
    ast.Sub: "-",
    ast.Mult: "*",
    ast.Div: "/"
}
    
    