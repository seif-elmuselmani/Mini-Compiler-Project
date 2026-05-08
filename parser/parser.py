from lexer.tokens import TokenType
from ast_nodes.ast import *

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, expected):
        raise Exception(f"Syntax Error on line {self.current_token.line}: Expected {expected}, got {self.current_token.type.name}")

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(token_type.name)

    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            statements.append(self.statement())
        return Program(statements)

    def statement(self):
        if self.current_token.type in (TokenType.INT, TokenType.STRING):
            return self.declaration()
        elif self.current_token.type == TokenType.ID:
            return self.assignment()
        elif self.current_token.type == TokenType.PRINT:
            return self.print_stmt()
        elif self.current_token.type == TokenType.IF:
            return self.if_stmt()
        elif self.current_token.type == TokenType.LBRACE:
            return self.block()
        else:
            self.error("Valid Statement (Declaration, Assignment, Print, If, or Block)")

    def declaration(self):
        var_type = self.current_token.value
        line = self.current_token.line
        self.eat(self.current_token.type) # eat 'int' or 'string'
        
        var_name = self.current_token.value
        self.eat(TokenType.ID)
        self.eat(TokenType.SEMI)
        return VarDecl(var_type, var_name, line)

    def assignment(self):
        var_name = self.current_token.value
        line = self.current_token.line
        self.eat(TokenType.ID)
        self.eat(TokenType.ASSIGN)
        expr = self.expression()
        self.eat(TokenType.SEMI)
        return Assign(var_name, expr, line)

    def print_stmt(self):
        line = self.current_token.line
        self.eat(TokenType.PRINT)
        expr = self.expression()
        self.eat(TokenType.SEMI)
        return PrintStmt(expr, line)

    def if_stmt(self):
        line = self.current_token.line
        self.eat(TokenType.IF)
        self.eat(TokenType.LPAREN)
        condition = self.expression()
        self.eat(TokenType.RPAREN)
        block = self.block()
        return IfStmt(condition, block, line)

    def block(self):
        self.eat(TokenType.LBRACE)
        statements = []
        while self.current_token.type != TokenType.RBRACE:
            statements.append(self.statement())
        self.eat(TokenType.RBRACE)
        return Block(statements)

    def expression(self):
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token.value
            line = self.current_token.line
            self.eat(self.current_token.type)
            node = BinOp(left=node, op=op, right=self.term(), line=line)
        return node

    def term(self):
        node = self.factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            op = self.current_token.value
            line = self.current_token.line
            self.eat(self.current_token.type)
            node = BinOp(left=node, op=op, right=self.factor(), line=line)
        return node

    def factor(self):
        token = self.current_token
        if token.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Literal(token.value, 'int', token.line)
        elif token.type == TokenType.STRING_LITERAL:
            self.eat(TokenType.STRING_LITERAL)
            return Literal(token.value, 'string', token.line)
        elif token.type == TokenType.ID:
            self.eat(TokenType.ID)
            return Variable(token.value, token.line)
        elif token.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expression()
            self.eat(TokenType.RPAREN)
            return node
        else:
            self.error("Integer, String, Identifier, or '('")
