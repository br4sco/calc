from parser import EOp


def collect_variables(expr):
    """Returns the set of variables that occurs in `expr`"""
    if isinstance(expr, str):
        return {expr}
    elif isinstance(expr, EOp):
        return collect_variables(expr.rand1).union(
            collect_variables(expr.rand2)
        )
    else:
        return set()


def _pretty_print_example(expr):
    names = collect_variables(expr)
    print(f"{names} is the set of names in {expr}")


# _pretty_print_example(None)  # set() is the set of names in None
# _pretty_print_example(EOp(Op.ADD, 1, 2))  # set() is the set of names in (+ 1 2)
# _pretty_print_example(
#     EOp(Op.ADD, 1, EOp(Op.SUB, 3, 2))
# )  # set() is the set of names in (+ 1 (- 3 2))
# _pretty_print_example(
#     EOp(Op.ADD, 1, "x")
# )  # {'x'} is the set of names in (+ 1 x)
# _pretty_print_example(
#     EOp(Op.ADD, "x", EOp(Op.SUB, 3, "y"))
# )  # {'x', 'y'} is the set of names in (+ x (- 3 y))
