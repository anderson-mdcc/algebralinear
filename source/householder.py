# imports
import numpy as np
from numpy import dot,diagonal,outer,identity,matmul,transpose,zeros_like,sign
from math import sqrt

norma = lambda x : np.sqrt(np.sum(np.square(x)))

# converter array 1d para vetor de coluna
def conv_col(x):
    x.shape = (1, x.shape[0])
    return x

def step_householder(A):
    ai = conv_col(A[:,0]).T
    tam_vet = ai.shape[0]
    n_ai = norma(ai)
    ei = zeros_like(ai)
    ei[0,0] = 1
    sign_a11 = sign(ai[0,0])
    vi = ai - (sign_a11 * n_ai * ei)
    Hi = identity(tam_vet) - 2 * ( (vi.dot(vi.T)) / (vi.T.dot(vi)) )
    return Hi

def checkDebug(flag, *args):
    if (flag):
        for arg in args:
            print(arg, end = '')
        print()

def qr_householder(A, debug=False):
    l, c = A.shape
    its = min(l,c)

    # aumenta uma linha e coluna na matriz
    # somente para manter o mesmo procedimento no laco
    Ai = identity(its + 1)
    Ai[1:,1:] = A

    # valor inicial de Q e R
    q = identity(its)
    r = A
    checkDebug(debug, '*******************************************************')
    for i in range(its - 1):
        checkDebug(debug, 'Iteração ', i, ': ***********************')
        # retira primeira linha e primeira coluna de Ai
        Ai = Ai[1:, 1:]
        checkDebug(debug, 'Ai (Entrada do step HouseHolder):\n', Ai)
        Hi = step_householder(Ai)
        Ai = Hi.dot(Ai)
        checkDebug(debug, 'Ai para proxima iteracao (Hi atual * Ai atual):\n', Ai)

        # coloca resultado Hi em Identidade para manter dimensao
        Ii = identity(its)
        Ii[i:,i:] = Hi

        checkDebug(debug, 'Ii (Saida do step_householder [Hi] com identidade na dimensao original de A):\n', Ii)
        r = matmul(Ii, r)
        q = matmul(q, Ii)
        checkDebug(debug, 'r:\n', r)
        checkDebug(debug, 'q:\n', q)
    checkDebug(debug, '***********************')
    return q, r