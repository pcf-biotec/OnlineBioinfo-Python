# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 13:55:19 2020

@author: Pedro C.

Strings
"""

seq = 'VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL'


"""
            Exercício 01
"""
#a) Retorne o tamanho da sequência
len(seq)

#b) Realize a contagem da ocorrência de um sequência de leucinas (LL)
seq.count('LL')

#c) Encontre na sequência as posições ocupadas por duas glicinas (GG) e duas argininas (RR). 
seq.find('GG','RR')

#d) Retorne os 100 primeiros aminoácidos da sequência.  
seq[:100]

#e) Substitua o trecho da sequência com a ocorrência de 3 serinas e 1 arginina  (SSSR) por alaninas.  
seq.replace('SSSR', 'A')

#f) Quebre a sequência no local onde a substituição foi realizada. 
seq.split('A')


"""
            Exercício 02
"""

texto = 'As  proteínas  são  cadeias  polipeptídicas  formadas  pela  ligação  peptídica  entre  resíduos  de  aminoácidos. Existem  20  tipos  de  aminoácidos  comumente  encontrados  nos  seres  vivos.  A  esses  aminoácidos,  foram atribuídas  abreviações  de  3  letras  e  símbolos  de  1  letra.  As  abreviações  de  3  letras  são  bastante  evidentes consistindo nas três primeiras letras do se nome.'

#a)Passe todo o texto para letras maiúsculas.
texto.upper()

#b)Passe todo o texto para letras minúsculas
texto.lower()

#c) Passe cada primeira letra de palavra em maiúsculo. 
texto.title()

#d)Transforme as letras maiúsculas em minúsculas e vice-versa.
texto.swapcase()


"""
            Exercício 03
            
"""
insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"

#a)Retorne o tamanho da sequência apresentada.
len(insulin_signal) 

#b)Quebre a sequência no trecho “LLALLALWG".
insulin_singal2 = insulin_signal.split('LLALLALWG')

#c) Concatene as sequências resultantes obtendo a seguinte sequência final MALWMRLLPPDPAAA
partA = insulin_singal2[0]
partB = insulin_singal2[1]

insulin_singal_final = str(partA)+str(partB)


#d) Substitua o trecho "DPAAA" por “LLALL”.
insulin_singal_final.replace("DPAAA","LLALL")


"""
            Exercício 04
            
 Com  base  na  sequência  de  DNA  GATGGAACTTGACGTAAACCTATATT  retorne  a  sequência  de  
 RNA correspondente sendo a mesma GAUGGAACUUGACGUAAACCUAUAUU
            
"""

DNA = 'GATGGAACTTGACGTAAACCTATATT'
RNA = '' 
RNA = DNA.replace('T', 'U')

RNA == 'GAUGGAACUUGACGUAAACCUAUAUU' #Conferindo se a sequência obtida é compatível com o proposto






























