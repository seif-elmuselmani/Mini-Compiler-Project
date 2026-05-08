from enum import Enum

class TokenType(Enum):
    # Keywords
    INT = 'INT'
    STRING = 'STRING'
    PRINT = 'PRINT'
    IF = 'IF'
    
    # Identifiers & Literals
    ID = 'ID'
    INTEGER = 'INTEGER'
    STRING_LITERAL = 'STRING_LITERAL'
    
    # Operators
    ASSIGN = 'ASSIGN'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MUL = 'MUL'
    DIV = 'DIV'
    
    # Punctuation
    SEMI = 'SEMI'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    LBRACE = 'LBRACE'
    RBRACE = 'RBRACE'
    
    EOF = 'EOF'

class Token:
    def __init__(self, type, value, line):
        self.type = type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)}, Line: {self.line})"
