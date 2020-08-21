import ast


def is_dunder(funcname):
    return funcname.startswith('__') and funcname.endswith('__')

def get_tree(file):
    with open(file, 'rb') as f:
        file_content = f.read()
        try:
            return ast.parse(file_content)
        except SyntaxError as e:
            print(e)

def get_varnames_ast(source):
    for node in ast.walk(source):
        if not isinstance(node, ast.Name):
            continue
        vname = node.id
        if not is_dunder(vname):
            yield vname
            
def get_funcnames_ast(source):
    for node in ast.walk(source):
        if not isinstance(node, ast.FunctionDef):
            continue
        fname = node.name
        if not is_dunder(fname):
            yield fname.lower()

def get_varnames_from_funcs_ast(source):
    for node in ast.walk(source):
        if not isinstance(node, ast.FunctionDef):
            continue
        yield from get_varnames_ast(node)