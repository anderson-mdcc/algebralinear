#!/usr/bin/env python3
import numpy.matlib
import numpy as np

# definindo as matrizes originais
mat = np.matrix('1 2 3 4;5 3 1 0;2 4 2 1;3 3 5 2;4 1 1 4;3 3 7 1')
mul = np.matrix('1 3 2 1').T
# print(mat)
# print(mul)

# imprimindo multiplicacao realizada por numpy
# print(mat.dot(mul))

# tamanho bloco (tbl x tbl)
tbl = 2

# tamanho matrizes
shape = np.shape(mat)
shapemul = np.shape(mul)
shaperes = (shape[0], shapemul[1])

for y in range(0, shape[0], tbl):
    for x in range(0, shape[1], tbl):
        z = mat[y:(y+tbl), x:(x+tbl)]
        print(z)
        print('')