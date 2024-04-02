from enum import StrEnum


class Op(StrEnum):
    """Enumerates integer operations. The string representation should
    correspond to the equivalent C infix operator."""

    ADD = "+"
    SUB = "-"


class Expr:
    """Base expression class."""

    pass


class EOp(Expr):
    """Binary operator AST node."""

    def __init__(self, rator, rand1, rand2):
        """`rator` is the operator and should be of type `Op`, `rand1` is the
        first operand and `rand2` is the second operand."""

        self.rator = rator
        self.rand1 = rand1
        self.rand2 = rand2

    def __str__(self):
        return f"({self.rator} {self.rand1} {self.rand2})"


def _parse(tokens):
    if not tokens:
        return None

    # Pop the first token
    token = tokens.pop(0)

    # Parses an operator. This function checks so that both operands are
    # defined.
    def parse_op(rator, rand1, rand2):
        if rand1 and rand2:
            return EOp(rator, rand1, rand2)
        return None

    # An integer token parses to an integer
    if isinstance(token, int):
        return token
    # An operator is followed by its two operands
    elif token == "+":
        return parse_op(Op.ADD, _parse(tokens), _parse(tokens))
    elif token == "-":
        return parse_op(Op.SUB, _parse(tokens), _parse(tokens))
    # All other strings are considered variables
    elif isinstance(token, str):
        return token
    else:
        return None


def parse(tokens):
    """Parses a seqence of `tokens` into an expression."""
    return _parse(tokens.copy())


def _pretty_print_example(tokens):
    expr = parse(tokens)
    if expr is None:
        print(f"Unable to parse: {tokens}")
    else:
        print(f"{tokens} parses to {expr}")


# _pretty_print_example(["+", 1, 2])  # ['+', '1', '2'] parses to (+ 1 2)
# _pretty_print_example(
#     ["+", 1, "-", 2, 3]
# )  # ['+', '1', '-', '2', '3'] parses to (+ 1 (- 2 3))
