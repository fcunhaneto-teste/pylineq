"""
To read an matrix from a terminal or file
"""
from os import system
from sys import platform, exit

if 'linux' in platform:
    def clear(): system('clear')
if 'win' in platform:
    def clear(): system('cls')


def read_terminal():
    """
    Insert the matrix from a terminal
    :return lines: a list that represents the array
    """
    clear()
    lines = []
    n = int(input('Entre com o número de linhas: '))
    print('\nDigite uma linha da matriz de cada vez, com os coeficientes separados por espaços, exemplo:')
    print('linha #: 2 4.2 7.5 8')
    print('*****************************************************************************************')
    for i in range(0, n):
        print("line", i + 1, ": ", end="")
        line = input()
        lines.append(line)

    lines = line_convert(lines)
    return lines


def read_file():
    """
    Insert the matrix from file
    :return: lines: a list that represents the array
    """
    clear()
    filename = input('Enter the file name : ')

    lines = []
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Could not find file {}".format(filename))

    lines = line_convert(lines)

    return lines


def line_convert(li):
    """
    Converts a list of string list into a list of numbers
    :param li: a list to convert
    :return: lines: list of list of numbers
    """
    lines = []
    for l in li:
        line = l.split()
        line = [float(s) for s in line]
        lines.append(line)

    return lines
