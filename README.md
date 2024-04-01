# A simple calculator interpreter and compiler

This code implements a simple calculator interpreter and compiler. Its purpose
is to illustrate the difference between an interpreter and a compiler.


The syntax of source program is defined by the following context-free grammar.

```
<Expr> ::= Num | Ident | <Op> <Expr> <Expr>
<Op> ::= + | -
```

where `Num` are integers and `Ident` are alphabetic identifiers. The operators
are written in polish notation (prefix form).

Example of a calc program:

```
+ - 3 2 1
```

which semantically corresponds to the expression

```
(3 - 2) + 1
```

using infix notation.

## Interpreting a program

To interpret a program first make the `calc` file executable, e.g., in the
terminal execute:

```
chmod +x calc
```

There is an example program in `prog1.txt`. To interpret this program run

```
./calc prog1.txt
```

the interpreter will query you for a value on the variable `x` and then compute
the result and print it to standard out.

## Compiling a program

To compile the same program to C. Run the following command

```
./calc --compile prog1.txt
```

this will compile the program to `prog1.c`. You can then compile this program
with, e.g., `gcc` with

```
gcc prog1.c -o prog1
```

To execute the compiled binary run the command

```
./prog1
```

from the terminal. The program has the same semantics as the interpreted
program.

## Implementation structure
The file `lexer.py` implement the lexer, the file `parser.py` implements the
parser, the file `interpreter.py` implements the interpreter, and the file
`codegen.py` implements the C code-generation. The file `variables.py` contains
variable related helper functions and the file `calc` is the main entry point to
the calc compiler/interpreter.
