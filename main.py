import sys
from lexer.lexer import Lexer
from parser.parser import Parser
from semantic.analyzer import SemanticAnalyzer

def run_compiler(file_path):
    print(f"\n======================================")
    print(f"--- Compiling {file_path} ---")
    print(f"======================================")
    try:
        with open(file_path, 'r') as file:
            code = file.read()
            
        print("1. Lexical Analysis & Parsing...")
        lexer = Lexer(code)
        parser = Parser(lexer)
        ast = parser.parse()
        print("   -> AST built successfully.")
        
        print("2. Semantic Analysis & Symbol Table generation...")
        analyzer = SemanticAnalyzer()
        analyzer.analyze(ast)
        print("   -> Semantic Analysis passed successfully! No semantic errors found.")
        
    except Exception as e:
        print(f"\n[COMPILER ERROR] {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_compiler(sys.argv[1])
    else:
        # Run example files if no argument is given
        examples = [
            "examples/valid.mc",
            "examples/error_redeclare.mc",
            "examples/error_undefined.mc",
            "examples/error_type.mc"
        ]
        for ex in examples:
            run_compiler(ex)
