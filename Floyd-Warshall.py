"""
title : Floyd-Warshall Algo implementation
author : $1D@1298
date : 01-11-2020
"""
import math
INF = math.inf


def matrix_input(vertex_count):
    A0 = []
    print('\n\nPlease input the A0 Matrix: \n')
    for i in range(vertex_count):
        A0.append([])
        for j in range(vertex_count):
            if j != i:
                n = input(f'A0[{i + 1}][{j + 1}]: ')
            else:
                n = '#'
            try:
                if j == i:
                    A0[i].append(0)
                else:
                    n = int(n)
                    A0[i].append(n)
            except ValueError:
                A0[i].append(INF)
    return A0


def pretty_print(name, matrix):
    print(f'{name}:')
    for row in matrix:
        print(row)
    print()


def relax(n, k, Akp):
    Akn = []
    for i in range(n):
        Akn.append([])
        for j in range(n):
            # print(Akp[i][j], Akp[i][k], Akp[k][j])
            Akn[i].append(min([
                Akp[i][j], Akp[i][k]+Akp[k][j]
            ]))
    return Akn


n = eval(input('Enter number of vertices: '))
A0 = matrix_input(n)
pretty_print('\nA0', A0)
A = A0
for i in range(n):
    A = relax(n, i, A)
    pretty_print(f'A{i+1}', A)
