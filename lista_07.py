# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:19:15 2020

@author: KUMA

Lista de Operadores
"""



"""
    Exercício 01
"""
sd_N  = (108.304 - 107.670)**2 + (100.827 - 101.359)**2 + (67.992 - 70.074)**2
sd_CA = (108.477 - 108.447)**2 + (100.389 - 100.389)**2 + (69.362 - 69.362)**2
sd_C  = (109.907 - 109.513)**2 + (100.555 - 101.011)**2 + (69,817 - 68.450)**2
sd_O  = (110.821 - 110.667)**2 + (100.799 - 100.572)**2 + (69.027 - 68.425)**2

print(sd_N, sd_CA, sd_C, sd_O)


"""
    Exercício 02
"""

GC = 0
GC_count = 0
seq = 'ATGATCTCGTAATTAACCGGAATTTTGGGCC'
for char in seq:
    if char == 'C' or char == 'G':
        GC_count += 1
        
#Contabilizando o percentual:

GC = (GC_count / len(seq)*100)
print('O conteudo GC da sequencia dada é: ',round(GC,2)) 
        
GC = 0
GC_count = 0
seq = 'GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA'
for char in seq:
    if char == 'C' or char == 'G':
        GC_count += 1
        
#Contabilizando o percentual:

GC = (GC_count / len(seq)*100)
print('O conteudo GC da sequencia dada é: ',round(GC,2)) 
        