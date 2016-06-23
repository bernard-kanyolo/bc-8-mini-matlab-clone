from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

from pygments.lexers import MatlabLexer
from parse import parse


matlab_completer = WordCompleter(
    ['inv', 'ones', 'zeros', 'random'], ignore_case=True)

variables = {"ans": None}


def main():
    history = InMemoryHistory()

    while True:
        try:
            text = prompt("MATLAB >>> ", lexer=MatlabLexer,
                          completer=matlab_completer, history=history)
            if text == "exit":
                break
            elif text == "help":
                print("coming soon")
            else:
                statement = text.split("=")
                if len(statement) == 1:
                    s = (parse(text.strip(), variables))
                    variables["ans"] = s
                    print("ans = \n\n\t{0}".format(s))
                elif len(statement) == 2:
                    v = statement[0].strip()
                    s = parse(statement[1].strip(), variables)

                    variables[v] = s
                    print("{0} = \n\n\t{1}".format(v, s))

        except (EOFError, KeyboardInterrupt, SystemExit):
            break
    print('GoodBye!')


if __name__ == '__main__':
    main()
