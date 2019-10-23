# imports
import numpy as np
from numpy import dot,diagonal,outer,identity,matmul,transpose,zeros_like
from math import sqrt

norma = lambda x : np.sqrt(np.sum(np.square(x)))

# converter array 1d para vetor de coluna
def conv_col(x):
    x.shape = (1, x.shape[0])
    return x

# matriz HH para vetor v
def HH(v):
    tam_de_v = v.shape[1]
    e1 = zeros_like(v)
    e1[0, 0] = 1
    vet = norma(v) * e1
    # funcao sinal (sign)
    if v[0, 0] < 0:
        vet = - vet
    u = (v + vet).astype(np.float32)
    m_identid = identity(tam_de_v)
    H = m_identid - ((2 * (u.T.dot(u))) / (u.dot(u.T)))
    return H

def it_qr_hh(q, r, iter, n):
    v = conv_col(r[iter:, iter])
    Hb = HH(v)
    H = identity(n)
    H[iter:, iter:] = Hb
    r = matmul(H, r)
    q = matmul(q, H)
    return q, r

A = np.matrix("3 7 8 9 12;5 -7 4 -7 8;1 1 -1 1 -1;4 3 2 1 7;9 3 2 5 4")
l, c = np.shape(A)


Q = identity(l)
R = A.astype(np.float32)
for i in range(min(l, c)):
    Q, R = it_qr_hh(Q, R, i, l)

np.set_printoptions(suppress=True)
#print('Matriz Q:\n', Q)
#print('Matriz R:\n', np.around(R, decimals=10))
#print('Validação:\n', np.allclose(A, np.dot(Q, R)))
#print('Matriz Q * R:\n', np.dot(Q, R))



#np.allclose(A, np.dot(q, r))
Qa = identity(A.shape[0])
print('Qa ini:\n', Qa)
ai = A
for i in range(1000):
    q, r = np.linalg.qr(ai)
    qt = transpose(q)
    ai = r * q
    Qa = Qa * q
print('Qa:\n', Qa)
print('q:\n', q)
print('r:\n', r)