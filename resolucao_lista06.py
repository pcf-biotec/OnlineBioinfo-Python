# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 18:22:36 2020

@author: Pedro C.

Dicionarios
"""


"""

Exercicio 01

"""
# a) Construa um dicionário onde os ids PDB sejam as chaves e o número de resíduos de aminoácidos sejam o valor.  

dic_PDB = { '1A8M':471,
            '1TNR':283,
            '2AZ5':592,
            '1TNF':471,
            '2TNF':468,
            '2TUN':942,
            '4TSV':150,
            '5TSW':900,
            '2E7A':471,
            '6RMJ':489
    }


# b) Imprima os valores contidos nos ids 2TNF e 2E7A.  
print(dic_PDB['2TNF'])
print(dic_PDB['2E7A'])

# c) Verifique e imprima o tamanho do dicionário construído  
len(dic_PDB)
print(len(dic_PDB))

# d) Obtenha e imprima a lista de todas as chaves do dicionário 
dic_PDB.keys()

# e) Obtenha e imprima a lista de todos os valores do dicionário 
dic_PDB.values()

# f) Obtenha e imprima uma lista de tuplas com todos os pares chave-valor. Cada dupla será um par ordenado (chave, valor). 
dic_PDB.items()
