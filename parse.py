from matrix import Matrix


def parse(expression, variables=None, concatenating=False):
    """take an expression, ie. part on the right of '=' and
    evaluate it, character by character
    """
    answer = None
    cursor = 0

    functions = ["inv", "ones", "zeros"]

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
                    answer = answer + digits
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
                raise ValueError("Unexpected white space")
        elif expression[cursor] == ';':
            if concatenating:
                peek, length = peekExpression(expression[cursor + 1:], ';]')
                peek_matrix = parse(expression=peek, concatenating=True)
                answer = answer.concat_vertical(peek_matrix)
                cursor += length + 1
            else:
                raise ValueError("Incorrect syntax use of ';'")
        elif expression[cursor] == '+':
            if concatenating:
                cursor += 1
            else:
                raise ValueError("Incorrect syntax")
        elif expression[cursor] == "'":
            pass
        elif expression[cursor].isalpha():
            # is a word character, need to check variables and keywords
            pass
        elif expression[cursor] == '(':
            pass
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


print(parse("[1;2;3;4;5;6;7;8;9]"))
