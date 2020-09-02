# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 16:00:08 2020

@author: Pedro C

Tuplas
"""

tupla_amino = ('A', 'C', 'D', 'E', 'F', 'G','H', 'I', 'K', 'L',
               'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')


# a) Conte e imprima o número de elementos contidos na tupla criada.
len(tupla_amino)
print(tupla_amino)
  
# b) Verifique e imprima se o aminoácido Serina (S) pertence à tupla.
'S' in tupla_amino 

# c) Crie uma segunda tupla contendo os elementos Prolina (P), Glicina (G), Asparagina (N), 
#    Tirosina (Y), Valina (V) e Triptofano (W).  
tupla_amino2 = ('P','G','N','Y','V','W')

# d) Some as tuplas construídas e imprima o resultado.
tupla_amino = tupla_amino + tupla_amino2
print(tupla_amino)
 
# e) Conte a ocorrência dos elementos Glicina (G), Asparagina (N) e Cisteína (C). 
tupla_amino.count('G')
tupla_amino.count('N')
tupla_amino.count('C')

#f) Retorne a posição do primeiro elemento Asparagina (N). 
tupla_amino.index('N')

# g) Retorne os 5 últimos elementos da tupla. 
tupla_amino[-5:]

