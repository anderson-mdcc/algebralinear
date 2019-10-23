#from source.funcoes import matmul as mm, norma
import numpy as np

def matmul(ma, mb):
    return ma.dot(mb)

norma = lambda x : np.sqrt(np.sum(np.square(x)))