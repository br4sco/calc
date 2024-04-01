import io


def lex(stream):
    """`lex(steam)` consumes a `stream` of characters and returns a list of
    tokens or throws an error on invalid input."""

    # Reads the stream, character-by-character, while the predicate is true, and
    # returns all read characters.
    def read_while(predicate):
        pos = stream.tell()
        n = 0
        while predicate(stream.read(1)):
            n += 1
        stream.seek(pos)
        return stream.read(n)

    # This will be our seqence of tokens
    tokens = []
    while True:
        char = stream.read(1)
        # We return the sequence of tokens when we have consumed the whole
        # stream.
        if not char:
            stream.close()
            return tokens
        # Ignore whitespace characters
        if char.isspace():
            pass
        # Operator tokens
        elif char == "+" or char == "-":
            tokens.append(char)
        # Integer tokens
        elif char.isdigit():
            tokens.append(int(char + read_while(lambda x: x.isdigit())))
        # Identifier tokens
        elif char.isalpha():
            tokens.append(char + read_while(lambda x: x.isalpha()))
        # If we reach this branch we have encountered an invalid token
        else:
            return None


# For testing purposes
def _pretty_print_example(inp):
    tokens = lex(io.StringIO(inp))
    if tokens is None:
        print(f"Unable to lex: {inp}")
    else:
        print(f"{inp} lexes to {tokens}")


# Examples, uncomment and interpret this file to print the output
# _pretty_print_example("+ 1 12")  # + 1 12 lexes to ['+', 1, 12]
# _pretty_print_example(
#     "- 12 + 2 3"
# )  # - 12 + 2 3 lexes to ['-', '12', '+', 2, 3]
# _pretty_print_example("+ 1 1 var")  # + 1 x lexes to ['+', 1, var]
