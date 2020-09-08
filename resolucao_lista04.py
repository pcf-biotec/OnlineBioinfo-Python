# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:10:48 2020

@author: Pedro C.


"""

"""

Exercício 01

"""
#a) Crie uma lista com esses identificadores, obtenha e imprima tamanho da lista criada.
ncbi = ['AAY66821.1', 'AAY66759.1', 'AAY66711.1', 'AAY66706.1', 'AAY66703.1', 'AAY66697.1',
        'AAY66696.1', 'AAY66682.1', 'AAY66647.1', 'AAY66625.1', 'AAY66623.1', 'AAY66620.1',
        'AAY66619.1', 'AAY66616.1', 'AAY66609.1', 'AAY66607.1', 'AAY66586.1', 'AAY66564.1',
        'AAY66562.1', 'AAY66561.1', 'AAY66558.1', 'AAY66544.1', 'AAY66542.1', 'AAY66539.1',
        'AAY66538.1', 'AAY66537.1', 'AAY66536.1', 'AAY66512.1', 'AAY66496.1', 'AAM93627.1',
        'AAM93626.1', 'AAY66506.1', 'AAM93587.1', 'AAY66811.1', 'AAY66620.1', 'AAY66555.1',
        'AAY66707.1', 'AAM93653.1', 'AAY66608.1', 'AAY66700.1', 'AAY66646.1', 'AAY66809.1',
        'AAK97814.1', 'AAK97810.1', 'AAY66594.1', 'AAY66685.1', 'AAY66571.1', 'AAY66865.1.'
        ]

len(ncbi)

#b) Verifique a presença dos seguintes identificadores

'AAY66682.1' in ncbi #True
'AAY66504.1' in ncbi #False
'AAY66640.1' in ncbi #False
'AAY66562.1' in ncbi #True
'AAY66816.1' in ncbi #False

#c) Obtenha e imprima o elemento presente na posição 10 da lista
print(ncbi[10])

#d) Insira os identificadores nas posições indicadas e imprima a lista fina:

ncbi.insert(11,'AAY66967.1')
ncbi.insert(21,'AAY66880.1')
ncbi.insert(16,'AAY66874.1')
ncbi
#e)  Verifique o elemento na posição 8 e em seguida o retire da lista e imprima a lista final.

ncbi.pop(8)
print(ncbi)


"""

Exercício 02

"""
#a) Crie uma lista contendo os valores acima e imprima a lista

doc_ptn = [-695.9, -884.3, -658.2, -917.9, -799.8, -842.1, -618.6, -726.6,
           -652.6, -594.8, -536.1, -788.2, -772.1, -676.9, -600.2, -575,
           -575.3,-603.4, -659.6, -715.3, -643.8, -703, -763.1, -712.1, -719,
           -574.2, -594.1, -700.3, -742.1, -621.9,-649.7, -663.3, -825.3,
           -849.3, -616.5, -675.1, -572.8,-624.2, -608, -615.3, -572.8, -665.3,
           -644.6,-788.9, -631.8, -707.4, -715.2, -728.2, -729, -642.1, -567.8,
           -596.5, -551.5, -735,  -805.5, -696.7, -617.9, -606.5, -658.8, 
           -667.8, -689.5, -728.4, -564, -725.8, -623.2,   -637, -570.9, 
           -646.6, -703.2, -722.3, -624.1, -655.4]

print(doc_ptn)

#b) Obtenha e imprima o tamanho da lista.
print(len(doc_ptn))

#c) Retorne o melhor score, considerando que o melhor modelo é aquele que apresenta a menor energia. 
print(min(doc_ptn))

#d) Retorne o pior score considerando que o mesmo apresenta a maior energia.  
print(max(doc_ptn))

#e) Remova o valor -575 da lista criada. 
doc_ptn.remove(-575)

#f) Ordene e imprima a lista criada em ordem crescente.  
doc_ptn.sort()
print(doc_ptn)

#g) Utilizando a lista ordenada na atividade anterior retorne o seu reverso (lista decrescente).
doc_ptn.reverse()
print(doc_ptn)






















