class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def declare(self, name, var_type):
        if name in self.symbols:
            return False
        self.symbols[name] = var_type
        return True

    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        if self.parent is not None:
            return self.parent.lookup(name)
        return None

    def __str__(self):
        return f"Symbols: {self.symbols}"
