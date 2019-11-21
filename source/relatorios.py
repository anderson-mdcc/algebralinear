from householder import *

A = np.matrix("3 7 8 9 12;5 -7 4 -7 8;1 1 -1 1 -1;4 3 2 1 7;9 3 2 5 4")
#np.random.seed(0)
#A = np.random.permutation(4*4).reshape((4,4)) + 1
#A = np.matrix("1 1 1 1 1;16 8 4 2 1;81 27 9 3 1;256 64 16 4 1;625 125 25 5 1")
l, c = np.shape(A)

np.set_printoptions(suppress=True)
#q, r = qr_householder(A, debug=True)
q, r = qr_householder(A)

ai = A
for a in range(1000):
    q, r = qr_householder(ai)
    ai = q.T.dot(ai).dot(q)

# print('A:\n', A)
# print('q:\n', np.around(r, decimals=10))
# print('r:\n', np.around(q, decimals=10))
# diag = np.diag(ai)
# diag.shape = (1, diag.shape[0])
# print('ai:\n', ai)
# print('autovalores iteracoes QR:\n', diag.T)
# print('autovalores (pela funcao do numpy):\n', np.linalg.eig(A))

print(step_householder(A))