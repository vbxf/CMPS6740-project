import ast

class MutationVisitor(ast.NodeTransformer):
    def __init__(self, op_str, var_name, value_str):
        self.op_str = op_str
        self.var_name = var_name
        self.value_str = value_str
        self.mutated = False

    def visit_AugAssign(self, node):
        op_map = {
            "+=": ast.Add(),
            "-=": ast.Sub(),
            "*=": ast.Mult(),
            "/=": ast.Div(),
            "**=": ast.Pow()
        }
        if self.op_str in op_map:
            node.op = op_map[self.op_str]
            self.mutated = True
        
        if self.var_name and isinstance(node.target, ast.Name):
            node.target.id = self.var_name
            self.mutated = True
            
        if isinstance(node.value, ast.Constant):
            try:
                node.value.value = int(self.value_str)
                self.mutated = True
            except:
                pass
        return node