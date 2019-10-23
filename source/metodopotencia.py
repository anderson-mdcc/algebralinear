# imports
import numpy as np
import math

class MetodoPotencia(object):
    def __init__(self, a, b, it):
        self.a = a
        self.x = x
        self.it = it
            
    def imprimeMatriz(self, msg, a, is_2d=False):
      print(msg)
      for l in range(0, len(a)):
          print('[', end='')
          if is_2d:
              for c in range(0, len(a[0])):
                  print(a[l][c], end=' ')
          else:
            print(a[l][0], end=' ')
          print(']')
            
      print("*"*49, '\n')
    
    
    def executaMP(self):
        maiorValor = None
        for i in range(self.it):
            print("*"*49, '\n')
            print("Iteração número {}".format(i))
            produtoAX = np.dot(self.a, self.x)
            self.imprimeMatriz("Produto A x", produtoAX)
            maiorValor = max(produtoAX.min(), produtoAX.max(), key=abs)
            self.x = 1.0 / maiorValor * produtoAX
            self.imprimeMatriz("Resultado de x", self.x)
    
    def calculaAutovalor(self):
        produto = np.dot(self.a, self.x)
        print(produto)
        autovalor = produto[0]/self.x[0]
        print("Autovalor encontrado = {}".format(autovalor))
    
     
    def iniciaMP(self):
        self.executaMP()
        self.calculaAutovalor()

A = np.matrix("3 7 8 9 12;5 -7 4 -7 8;1 1 -1 1 -1;4 3 2 1 7;9 3 2 5 4")
x = np.ones(3)
print(A)
print(x)
