from parser import Op, EOp


def interpret(env, expr):
    """Interprets an expression `expr` to a number in the environment `env`,
    where `env` is a dictionary from variable names to integer values."""
    if not expr:
        return None

    # An integer is a value
    if isinstance(expr, int):
        return expr
    # If we encounter a variable we look up its value in the environment
    elif isinstance(expr, str):
        return env[expr]
    # Here we interpret operations
    elif isinstance(expr, EOp):
        if expr.rator == Op.ADD:
            return interpret(env, expr.rand1) + interpret(env, expr.rand2)
        elif expr.rator == Op.SUB:
            return interpret(env, expr.rand1) - interpret(env, expr.rand2)
        else:
            None
    # We never expect to reach this branch in a parsed program
    else:
        return None


def _pretty_print_example(expr):
    val = interpret({"x": 4}, expr)
    if val is None:
        print(f"Unable to interpret: {expr}")
    else:
        print(f"{expr} evaluates to {val}")


# _pretty_print_example(EOp(Op.ADD, 1, 2))  # (+ 1 2) evaluates to 3
# _pretty_print_example(
#     EOp(Op.ADD, 1, EOp(Op.SUB, 3, 2))
# )  # (+ 1 (- 3 2)) evaluates to 2
# _pretty_print_example(EOp(Op.ADD, 1, "x"))  # (+ 1 x) evaluates to 5
