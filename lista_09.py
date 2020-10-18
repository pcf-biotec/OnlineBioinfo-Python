# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 21:53:35 2020

@author: Pedro C.

Lista Estrutura de Repetição
"""

"""
    Exercício 01
"""
for i in range(0,150): 
    C = 5/9*(i-32) 
    
"""
    Exercício 02   -> Rever
"""

seq1 = 'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN'
seq2 = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
seq3 = 'ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN'

RNA = {'U','C','A','G'}
DNA = {'A','G','T','C'}
PTN = {'A','C','D','E',
       'F','G','H','I',
       'K','L','M','N',
       'P','Q','R','S',
       'T','V','W','Y'}

for char in seq1:
    if (seq1 in RNA) and (seq1 not in DNA) and (seq1 not in PTN):
        print('É um RNA')
    if (seq1 in DNA) and (seq1 not in RNA) and (seq1 not in PTN):
        print('É um DNA')
    if (seq1 in PTN) and (seq1 not in DNA) and (seq1 not in RNA):
        print('É uma PROTEINA')
        
"""
    Exercício 03
"""
DNA_norm = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
DNA_rev = ''
for char in DNA_norm:
    if char == 'T':
        DNA_rev += 'A'

    if char == 'A':
        DNA_rev += 'T'
        
    if char == 'G':
        DNA_rev += 'C'
        
    if char == 'C':
        DNA_rev += 'G'
                                
"""
    Exercício 04
"""

num = int(input('Insira um número de 1 a 15: '))
fat = 1

for i in range(1, num + 1):
    fat = fat * i
print(fat)

"""
    Exercício 05
"""

num = int(input('Insira um número de 1 a 15: '))

for i in range(0,11):
    tab = num*i
    print(tab)    

"""
    Exercício 06
"""
massa_tot = 0
seq = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'
massas = {'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259,
          'F':147.06841, 'G':57.02146, 'H':137.05891, 'I':113.08406,
          'K':128.09496, 'L':113.08406, 'M':131.04049, 'N':114.04293,
          'P':97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203,
          'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333
          }

for char in seq:
    for key in massas:
        if key == char:
            massa_tot += massas[key]

print('A massa molar da sequência dada é: ', round(massa_tot, 4))

"""
    Exercício 07
"""

# Imprimindo a menor sequência:
seqs = ['KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC',
        'ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF',
        'ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR',
        'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF',
        ]

for i in range(len(seqs)):
    if len(seqs[1-i]) < len(seqs[i]):
        menor_seq = seqs[1-i]

print('A maior sequencia é a ',menor_seq)    
   
#   Imprimindo maior sequência:
seqs = ['KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC',
        'ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF',
        'ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR',
        'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF',
        ]

maior_seq = 0
seq_final =''
for char in seqs:
    if len(char) > maior_seq:
        maior_seq = len(char)
        seq_final = char
print('A maior sequencia é: \n',seq_final)
##### Método alternativo
print('A maior sequencia é: \n',max(seqs))
    
# Imprimindo a média dos comprimentos:
seqs = ['KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC',
        'ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF',
        'ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN',
        'ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR',
        'ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF',
        ]

tot_len = 0
for char in seqs:
    tot_len += len(char)
m = tot_len/len(seqs)

print('A média do comprimento das sequências é: ', round(m, 4))

# Imprimindo as sequência que esta na mediana:
seqs_ordem = sorted(seqs, key=len)
n = len(seqs_ordem)

if n % 2 == 0:
    mediana1 = seqs_ordem[n//2]
    mediana2 = seqs_ordem[n//2 - 1]
    mediana = (mediana1 + mediana2)/2     
    
else:
    mediana = seqs_ordem[n//2]

print('A mediana é: ',mediana)

"""
    Exercício 08
"""
molec1 = [0,0,1,0,0,1,1,0,1,1,0,1]
molec2 = [0,1,0,0,1,1,0,1,1,0,0,0]

AndB = 0
AorB = 0


for i in range(len(molec1)):
    if molec1[i] and molec2[i] == 1:
        # print(i+1)
        AndB += 1
    if molec1[i] or molec2[i] == 1:
        AorB += 1
        # print(i+1)

print('A distancia Tanimoto das duas moléculas é: ',round(AndB/AorB,4))        

