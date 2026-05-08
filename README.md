# 🚀 Custom Programming Language Compiler

A robust, educational programming language compiler implemented in Python. This project covers the core phases of a compiler, from Lexical Analysis to Semantic Validation, supporting nested scopes and static typing.

## 📌 Project Overview
This compiler translates a custom C-like language with features such as:
- **Static Typing**: `int` and `string` data types.
- **Lexical Scoping**: Support for nested blocks `{ }` with proper symbol management.
- **Control Flow**: `if` statements for conditional execution.
- **Expression Evaluation**: Arithmetic operations with full operator precedence (PEMDAS).
- **Semantic Validation**: Detection of redeclarations, undefined variables, and type mismatches.

## 🏗️ Architecture
The compiler follows a modular pipeline:
1. **Lexer**: Tokenizes raw source code using a manual scanner.
2. **Parser**: Implements a **Recursive Descent** strategy to build an **Abstract Syntax Tree (AST)**.
3. **Symbol Table**: Manages identifiers using a linked-list of scopes (parent pointers).
4. **Semantic Analyzer**: Performs a visitor-pattern traversal on the AST to enforce language rules.

## 📂 Project Structure
```text
├── lexer/
│   ├── lexer.py       # Tokenization logic
│   └── tokens.py      # Token definitions
├── parser/
│   └── parser.py      # Recursive Descent Parser
├── ast_nodes/
│   └── ast.py         # AST node definitions
├── symbol_table/
│   └── symbol_table.py # Scoping and variable management
├── semantic/
│   └── analyzer.py    # Semantic rule validation
├── examples/          # Sample programs (.mc files)
└── main.py            # Entry point
```

## 🚀 Getting Started
### Prerequisites
- Python 3.8+

### Running the Compiler
To compile and run the provided examples:
```bash
python main.py
```

To compile a specific file:
```bash
python main.py examples/valid.mc
```

## 📜 Grammar (CFG)
The language follows a context-free grammar defined in EBNF:
```ebnf
Program     ::= Statement*
Statement   ::= Declaration | Assignment | PrintStmt | IfStmt | Block
Declaration ::= DataType ID ";"
Assignment  ::= ID "=" Expression ";"
Expression  ::= Term (('+' | '-') Term)*
Term        ::= Factor (('*' | '/') Factor)*
Factor      ::= INTEGER | STRING_LITERAL | ID | '(' Expression ')'
```

## 🛡️ Error Handling
The compiler is designed to detect and report clear errors:
- **Lexical Errors**: Unterminated strings or invalid characters.
- **Syntax Errors**: Improper code structure (missing semicolons, unmatched braces).
- **Semantic Errors**: Variable redeclaration or usage of undefined variables.

---
*Developed for University Compiler Course - 2026*
