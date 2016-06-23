from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

from pygments.lexers import MatlabLexer


matlab_completer = WordCompleter(
    ['inv', 'ones', 'zeros', 'random'], ignore_case=True)


def main():
    history = InMemoryHistory()

    while True:
        try:
            text = prompt("MATLAB >>> ", lexer=MatlabLexer,
                          completer=matlab_completer, history=history)
            print('You entered: {}'.format(text))
        except (EOFError, KeyboardInterrupt, SystemExit):
            break
    print('GoodBye!')


if __name__ == '__main__':
    main()
