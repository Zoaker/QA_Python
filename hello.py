import readline
import ParseArg

MAIN_COMMANDS = ['link', 'check', 'report', 'gds', 'lib', 'lef', 'tf', 'library', 'version', 'set_parameter']




def complete(text, state):

    for cmd in MAIN_COMMANDS:
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1
#
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

while True:
    command = input('>>> QA: ')
    try:
        args = ParseArg.Parse(command.split())
        print(args)
    except SystemExit:
        print ()