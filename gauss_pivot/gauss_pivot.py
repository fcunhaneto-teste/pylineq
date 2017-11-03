"""
Resolve um sistema de equações lineares atravês da matriz extendida pelo
sistema de eliminação de Gauss com pivotação parcial.
"""
import numpy as np
from os import system
from sys import path, platform

path.append('../')

from readmatrix import readmatrix as rd


if 'linux' in platform:
    def clear(): system('clear')
if 'win' in platform:
    def clear(): system('cls')


def gauss_pivot(mat):
    a = np.array(mat)
    n, m = np.shape(a)

    for i in range(n-1):
        maxi = np.amax(abs(a[:,i:i+1]))
        line = np.argmax(abs(a[:,i:i+1]))

        if maxi == 0:
            print('Sistema não têm solução única')
            exit(0)

        if line != i:
            aux = np.array(a[i])
            a[i] = a[line]
            a[line] = aux

        for j in range(i+1, n):
            mij = a[j][i] / a[i][i]
            a[i] = mij * a[i]
            a[j] = a[j] - a[i]
    print('\nMatrix triangular:\n')
    print(a, '\n')
    calcular_x(a)


def calcular_x(a):
    n, m = np.shape(a)
    x = np.empty(n, dtype=float)
    x[n-1] = a[n-1][m-1] / a[n-1][m-2]

    for i in range(n-2, -1, -1):
        soma = 0
        for j in range(m-2, i, -1):
            soma = soma + (a[i][j] * x[j])
        x[i] = (a[i][m-1] - soma) / a[i][i]

    for i in range(n):
        print('x{0:d} = {1:.4f}'.format(i, x[i]), end='')

    print()


clear()
print('Escolha uma opção\n')
print('1 - Entrar com a matriz estendida pelo terminal.')
print('2 - Entrar com a matriz estendida na forma de um arquivo.\n')

try:
    op = int(input('Entre com sua opção: '))
except ValueError:
    print("Opção invalida!!!")
    exit(1)


if op == 1:
     a = rd.read_terminal()
elif op == 2:
    a = rd.read_file()
else:
    print('Opção invalida!!!')
    exit(1)

gauss_pivot(a)