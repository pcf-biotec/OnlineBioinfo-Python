# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:06:02 2020

@author: Pedro C.

Sets
"""


"""

Exercício 01

"""

conj1 = {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7, 4.6, 5.2, 5.3}
conj2 = {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5, 1.0, 1.3, 5.4}
conj3 = {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9, 9.3, 9.5}

# a) Verifique as diferenças entre os conjuntos (1,2) (1,3) e (2,3)  
conj1.difference(conj2) #diferenças entre conjuntos 1 e 2
conj1.difference(conj3) #diferenças entre conjuntos 1 e 3
conj2.difference(conj3) #diferenças entre conjuntos 2 e 3

# b) Retorne as intersecções entre (1,2) (1,3) e (2,3)  
conj1.intersection(conj2) #uniao entre conjuntos 1 e 2
conj1.intersection(conj3) #uniao entre conjuntos 1 e 3
conj2.intersection(conj3) #uniao entre conjuntos 2 e 3


# c) Insira todos os elementos do conjunto 2 e 3 no conjunto 1 
conj3.update(conj1,conj2)

# d) Retorne o tamanho do conjunto formado pela tarefa (c).  
len(conj3)



"""

Exercício 02

"""

A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27} 
B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24} 
C = {2, 6, 10, 18, 20} 
D = {1, 30, 5, 11, 17, 16, 22, 26} 


# a) Verifique a interseção e diferença entre o conjunto A e B.  
A.intersection(B)

# b) Verifique se o conjunto A e B são disjuntos ao conjunto D 
A.isdisjoint(D)
B.isdisjoint(D)

# c) Retorne se o conjunto C é subconjunto de A e B  
C.issubset(A)
C.issubset(B)

# d) Acrescente os elementos 18, 23, 25, 63 no conjunto D
D.update({18,23,25,63})
print(D)


