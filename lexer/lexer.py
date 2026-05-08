import re
from lexer.tokens import Token, TokenType

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def advance(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.line += 1
            self.advance()

    def string_literal(self):
        result = ''
        self.advance() # skip opening quote
        while self.current_char is not None and self.current_char != '"':
            result += self.current_char
            self.advance()
        
        if self.current_char is None:
            raise Exception("Lexical Error: Unterminated string literal")
            
        self.advance() # skip closing quote
        return Token(TokenType.STRING_LITERAL, result, self.line)

    def number(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(TokenType.INTEGER, int(result), self.line)

    def _id(self):
        result = ''
        while self.current_char is not None and self.current_char.isalnum():
            result += self.current_char
            self.advance()
        
        # Check if the identifier is a keyword
        keywords = {
            'int': TokenType.INT,
            'string': TokenType.STRING,
            'print': TokenType.PRINT,
            'if': TokenType.IF
        }
        
        token_type = keywords.get(result, TokenType.ID)
        return Token(token_type, result, self.line)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
                
            if self.current_char == '"':
                return self.string_literal()
                
            if self.current_char.isalpha():
                return self._id()
                
            if self.current_char.isdigit():
                return self.number()
                
            if self.current_char == '=':
                self.advance()
                return Token(TokenType.ASSIGN, '=', self.line)
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+', self.line)
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-', self.line)
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL, '*', self.line)
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV, '/', self.line)
            if self.current_char == ';':
                self.advance()
                return Token(TokenType.SEMI, ';', self.line)
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(', self.line)
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')', self.line)
            if self.current_char == '{':
                self.advance()
                return Token(TokenType.LBRACE, '{', self.line)
            if self.current_char == '}':
                self.advance()
                return Token(TokenType.RBRACE, '}', self.line)

            raise Exception(f"Lexical Error on line {self.line}: Invalid character '{self.current_char}'")

        return Token(TokenType.EOF, None, self.line)
