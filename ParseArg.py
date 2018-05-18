import argparse


def Parse(list):
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(prog=">>> QA:", description="Standard Library Check Platform")

    parser.add_argument('method', nargs='*', default='n', help='link/check/report/set_parameter -gds/-lef/-lib/rules/sets')

    parser.add_argument('-library', dest='library name', nargs='?', default='default', help='define library name')
    parser.add_argument('-version', dest='version name', nargs='?', default='default', help='define version name')

    parser.add_argument('-gds', nargs='?', help='define gds file')
    parser.add_argument('-lef', nargs='?', help='define lef file')
    parser.add_argument('-lib', nargs='?', help='define lib file')
    parser.add_argument('-tf',  nargs='?', help='define gds technology file')

    args = parser.parse_args(list)

    return args