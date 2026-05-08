class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class Block(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VarDecl(ASTNode):
    def __init__(self, var_type, var_name, line):
        self.var_type = var_type # 'int' or 'string'
        self.var_name = var_name # The identifier string
        self.line = line

class Assign(ASTNode):
    def __init__(self, var_name, expr, line):
        self.var_name = var_name
        self.expr = expr
        self.line = line

class PrintStmt(ASTNode):
    def __init__(self, expr, line):
        self.expr = expr
        self.line = line

class IfStmt(ASTNode):
    def __init__(self, condition, block, line):
        self.condition = condition
        self.block = block
        self.line = line

class BinOp(ASTNode):
    def __init__(self, left, op, right, line):
        self.left = left
        self.op = op # '+', '-', '*', '/'
        self.right = right
        self.line = line

class Literal(ASTNode):
    def __init__(self, value, value_type, line):
        self.value = value
        self.value_type = value_type # 'int' or 'string'
        self.line = line

class Variable(ASTNode):
    def __init__(self, name, line):
        self.name = name
        self.line = line
