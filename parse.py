from matrix import Matrix


def parse(expression, variables=None, concatenating=False):
    """take an expression, ie. part on the right of '=' and
    evaluate it, character by character
    """
    answer = None
    cursor = 0
    varis = ()
    if variables:
        varis = tuple(variables.keys())

    functions = ["inv(", "ones(", "zeros("]

    while(cursor < len(expression)):
        if expression[cursor].isdigit():
            digits, length = digits_consecutive(expression[cursor:])
            if concatenating:
                if answer:
                    answer = answer.concat_horizontal(Matrix(digits))
                else:
                    answer = Matrix(digits)
            else:
                if answer:
                    answer = answer + Matrix(digits)
                else:
                    answer = Matrix(digits)
            cursor += length
        elif expression[cursor] == '[':
            concatenating = True
            cursor += 1
        elif expression[cursor] == ']':
            concatenating = False
            cursor += 1
        elif expression[cursor] == ',':
            if concatenating:
                cursor += 1
            else:
                raise ValueError("Incorrect syntax use of ','")
        elif expression[cursor] == " ":
            if concatenating:
                cursor += 1
            else:
                cursor += 1
                #raise ValueError("Unexpected white space")
        elif expression[cursor] == ';':
            if concatenating:
                peek, length = peekExpression(expression[cursor + 1:], ';]')
                peek_matrix = parse(peek, variables, concatenating=True)
                answer = answer.concat_vertical(peek_matrix)
                cursor += length + 1
            else:
                raise ValueError("Incorrect syntax use of ';'")
        elif expression[cursor] == '+':
            if concatenating:
                raise ValueError("Incorrect use of '+'")
            else:
                cursor += 1
        elif expression[cursor] == "'":
            pass
        elif expression[cursor:].startswith("inv("):
            # function for inv()
            peek, length = peekExpression(expression[cursor + 4:], ')')
            peek_matrix = parse(peek, variables).inverse()

            if concatenating:
                if answer:
                    answer = answer.concat_horizontal(peek_matrix)
                else:
                    answer = peek_matrix
            else:
                if answer:
                    answer = answer + peek_matrix
                else:
                    answer = peek_matrix

            cursor += length + 4
        elif expression[cursor:] == '(':
            peek, length = peekExpression(expression[cursor + 1:], ')')
            peek_matrix = parse(peek, variables, concatenating)
            if concatenating:
                if answer:
                    answer = answer.concat_horizontal(peek_matrix)
                else:
                    answer = peek_matrix
            else:
                if answer:
                    answer = answer + peek_matrix
                else:
                    answer = peek_matrix

            cursor += length + 1
        elif expression[cursor] == ')':
            cursor += 1
        elif expression[cursor:].startswith(varis):
            length = 1
            for v in varis:
                if expression[cursor:].startswith(v):
                    length = len(v)
                    peek_matrix = variables[v]
                    if concatenating:
                        if answer:
                            answer = answer.concat_horizontal(peek_matrix)
                        else:
                            answer = peek_matrix
                    else:
                        if answer:
                            answer = answer + peek_matrix
                        else:
                            answer = peek_matrix
            cursor += length

        else:
            raise ValueError("Incorrect syntax")

    return answer


def peekExpression(rem_expression, terminate_with):
    """gets an expression by peeking forward from the cursor's position
    """
    end = 0
    for index, char in enumerate(rem_expression):
        if char in terminate_with:
            end = index
            break
    else:
        raise ValueError("No closing bracket found")

    return (rem_expression[:end], end)


def digits_consecutive(text):
    """gets consecutive digits as an int or float
    """
    end = 0
    for index, char in enumerate(text):
        if char.isdigit() or char == ".":
            pass
        else:
            end = index
            break
    else:
        end = len(text)

    nums = text[:end]

    try:
        return (int(nums), end)
    except:
        return (float(nums), end)

test_dict = {"a": Matrix([[1, 2], [3, 4]]), "b": Matrix([[1, 1], [1, 1]])}
print(parse("a + 1", test_dict, concatenating=False))
