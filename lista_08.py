# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 13:44:11 2020

@author: KUMA

Lista de Estruturas Condicionais
"""

"""
    Exercício 01
"""

seq_A = 'LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK'
seq_B = 'KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS'
seq_C = 'CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR'

l_seqs = [seq_A, seq_B, seq_C]
len(l_seqs[1])

if len(seq_A) > 80: 
    print(seq_A)    

if (len(seq_B) > 80):
    print(seq_B)

if len(seq_C) > 80:
    print(seq_C)    
    
"""
    Exercício 02
"""

med_seqs = (len(seq_A) + len(seq_B) + len(seq_C))/3

for i in range(len(l_seqs)):
    if len(l_seqs[i]) > med_seqs:
        print(l_seqs[i])

"""
    Exercício 03
"""

# forma 01
if 'H' in seq_A:
    if 'P' not in seq_A:    
        print(seq_A)
        
if 'H' in seq_B:
    if 'P' not in seq_B:    
        print(seq_B)
        
if 'H' in seq_C:
    if 'P' not in seq_C:    
        print(seq_C)


# forma 02
for char in l_seqs:
    if 'H' in l_seqs:
        if 'P' not in l_seqs:
            print(l_seqs)


"""
    Exercício 04
"""

for i in range(len(l_seqs)):
    if len(l_seqs[i]) > len(l_seqs[1-i]):
        print(l_seqs[i])

"""
    Exercício 05
"""
for i in range(len(l_seqs)):
    if len(l_seqs[i]) < len(l_seqs[1-i]):
        print(l_seqs[i])
        print(l_seqs[i-1])
        print(l_seqs[i-2])




        
        
        
        
        
        
        
        
        
        
        
        
        