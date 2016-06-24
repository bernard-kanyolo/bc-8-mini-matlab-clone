from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter
from numpy.linalg import LinAlgError

from pygments.lexers import MatlabLexer
from parse import parse

import pickle

matlab_completer = WordCompleter(
    ['inv', 'ones', 'zeros', 'exit', 'help', 'workspace', 'save', 'load', "'"], ignore_case=True)

variables = {"ans": None}


def main(variables):
    history = InMemoryHistory()

    print("\n\n\n")
    print("----------------------------------------------------")
    print("----------     Welcome to Mini Matlab     ----------")
    print("----------------------------------------------------")
    print("\n\n\n")

    while True:
        try:
            text = prompt("MATLAB >>> ", lexer=MatlabLexer,
                          completer=matlab_completer, history=history)
            text = text.lower()
            if text == "exit":
                break
            elif text == "help":
                print("\nPress <TAB> to see available commands\n")
            elif text == "workspace":
                for key in variables:
                    print("\n{0} = \n".format(key))
                    print(variables[key])
            elif text.strip().startswith("save > "):
                index = text.find(">") + 2
                filename = text[index:]
                save_workspace(filename, variables)
                print("saved\n\n")
            elif text.strip().startswith("load < "):
                index = text.find("<") + 2
                filename = text[index:]
                variables = load_workspace(filename)
                print("loaded\n\n")
            else:
                try:
                    statement = text.split("=")
                    if len(statement) == 1:
                        s = (parse(text.strip(), variables))
                        variables["ans"] = s
                        print("ans = \n\n{0}".format(s))
                    elif len(statement) == 2:
                        v = statement[0].strip()
                        s = parse(statement[1].strip(), variables)

                        variables[v] = s
                        print("{0} = \n\n{1}".format(v, s))
                except ValueError as error:
                    print(str(error))
                except LinAlgError as error:
                    print("Inverse Error: {0}".format(str(error)))

        except (EOFError, KeyboardInterrupt, SystemExit):
            break
    print('\n\nThank you for using Mini Matlab.\nGoodBye!\n')


def save_workspace(filename, vars):
    """save the variables in the namespace to a pickle file
    """
    with open(filename, 'wb') as handler:
        pickle.dump(vars, handler)


def load_workspace(filename):
    """load from file into variables
    """
    variables = {}
    with open(filename, 'rb') as handler:
        variables = pickle.load(handler)

    return variables

if __name__ == '__main__':
    main(variables)
