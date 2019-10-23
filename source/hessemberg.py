#Hessenberg
from funcoes import *
#http://mathworld.wolfram.com/HessenbergMatrix.html

A = np.matrix("3 7 8 9 12;5 -7 4 -7 8;1 1 -1 1 -1;4 3 2 1 7;9 3 2 5 4")
l, c = np.shape(A)


Ai = A
for i in range(10000):
    q, r = np.linalg.qr(Ai)
    Ai = r.T.dot(q)

print('Ai:\n', Ai)
print('q:\n', q)
print('r:\n', r)
print('qr:\n', q.dot(r))