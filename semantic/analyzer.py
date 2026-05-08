from ast_nodes.ast import *
from symbol_table.symbol_table import SymbolTable

class SemanticAnalyzer:
    def __init__(self):
        self.current_scope = SymbolTable()

    def analyze(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method defined in SemanticAnalyzer.")

    def visit_Program(self, node):
        for stmt in node.statements:
            self.analyze(stmt)

    def visit_Block(self, node):
        # Enter new block scope
        previous_scope = self.current_scope
        self.current_scope = SymbolTable(parent=previous_scope)
        
        for stmt in node.statements:
            self.analyze(stmt)
            
        # Exit block scope
        self.current_scope = previous_scope

    def visit_VarDecl(self, node):
        # Check for variable redeclaration
        success = self.current_scope.declare(node.var_name, node.var_type)
        if not success:
            raise Exception(f"Semantic Error on line {node.line}: Variable '{node.var_name}' is already declared in this scope.")

    def visit_Assign(self, node):
        # Check if variable is defined
        var_type = self.current_scope.lookup(node.var_name)
        if var_type is None:
            raise Exception(f"Semantic Error on line {node.line}: Variable '{node.var_name}' is not defined.")
            
        expr_type = self.analyze(node.expr)
        
        # Check for type mismatch
        if var_type != expr_type:
            raise Exception(f"Semantic Error on line {node.line}: Type mismatch. Cannot assign '{expr_type}' to '{var_type}' variable '{node.var_name}'.")

    def visit_PrintStmt(self, node):
        self.analyze(node.expr)

    def visit_IfStmt(self, node):
        cond_type = self.analyze(node.condition)
        if cond_type != 'int':
            raise Exception("Semantic Error: 'if' condition must be an 'int'")
        self.analyze(node.block)

    def visit_BinOp(self, node):
        left_type = self.analyze(node.left)
        right_type = self.analyze(node.right)
        
        # Check if operands have the same type
        if left_type != right_type:
            raise Exception(f"Semantic Error on line {node.line}: Type mismatch in binary operation. Cannot operate '{left_type}' {node.op} '{right_type}'.")
            
        # Optional: restrict operations on strings (only concatenation allowed)
        if left_type == 'string' and node.op != '+':
            raise Exception(f"Semantic Error on line {node.line}: Invalid operation '{node.op}' for strings. Strings only support '+'.")
            
        return left_type

    def visit_Literal(self, node):
        return node.value_type

    def visit_Variable(self, node):
        # Check if variable is defined before usage
        var_type = self.current_scope.lookup(node.name)
        if var_type is None:
            raise Exception(f"Semantic Error on line {node.line}: Variable '{node.name}' used before declaration.")
        return var_type
