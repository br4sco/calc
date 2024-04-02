from calcparser import EOp


def codegen(variables, expr):
    # Generates main function and add all necessary includes. `variables` is a
    # sequence of variable names occuring in `expr` and `expr` is a calc
    # expression.
    def gen_main(body):
        return """\
#include <stdio.h>
int main() {{
   {body}
}}
""".format(
            body=body
        )

    # Generates user query for variable value
    def gen_var_def(var):
        return """
    int {var};
    printf(\"Give an integer value to {var}: \");
    scanf(\"%d\", &{var});""".format(
            var=var
        )

    # Generate user queries for variable values.
    var_defs = "\n".join([gen_var_def(var) for var in variables])

    # Expression generation
    def gen_expr(expr):
        if isinstance(expr, int) or isinstance(expr, str):
            return expr
        elif isinstance(expr, EOp):
            lhs = gen_expr(expr.rand1)
            rhs = gen_expr(expr.rand2)
            if lhs and rhs:
                return f"({lhs} {expr.rator} {rhs})"
            return None
        else:
            return None

    expr = gen_expr(expr)

    if expr:
        # Generate main body
        body = """\
{var_defs}

    printf(\"result = %d\\n\", {expr});""".format(
            var_defs=var_defs, expr=expr
        )
        return gen_main(body)

    return None
