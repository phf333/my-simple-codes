

import fileinput

## EXERCICIO 1

print "TOTAL DE PALAVRAS: "

palavras= 0
for x in fileinput.input("Palavras.txt"):
    palavras= palavras + 1
print palavras

## EXERCICIO 2


print "MAIORES PALAVRAS: "
a=0
for x in fileinput.input("Palavras.txt"):
    xx= x.strip()
    if len(xx)>a:
        a=len(xx)
print a
for x in fileinput.input("Palavras.txt"):
    xx= x.strip()
    if len(xx)==a:
        print xx    

## EXERCICIO 3


print "PALINDROMOS: "

for x in fileinput.input("Palavras.txt"):
    xx= x.strip()
    if xx==xx[::-1] and len(xx) >2:
        print xx

## EXERCICIO 4


print "PALAVRAS COM PADRAO S**V***R*: "

for x in fileinput.input("Palavras.txt"):
    xx= x.strip()
    if len(xx) ==10:
        if xx[0]== "S" and xx[3] == "V" and xx[7] == "R":
            print xx

## DESAFIO


print "~DESAFIO DAS PALAVRAS~"

import fileinput
import string
import re

palavras = []
temp = []
resposta = []

for i in fileinput.input("Palavras.txt"):
    palavras.append(str(i)[0:-1])

print "Bem vindo ao buscador de palavras.\nEle funciona com padrões analogos a S**V***R**, onde * é uma letra qualquer.\nUma busca por A*** retornaria palavras começando com A seguido de 3 letras quaisqer"
padrao = raw_input('Digite o padrão que deseja buscar:')

padrao2 = padrao.replace("*", ".") # Pequeno ajuste já que o charactere coringa para expressões
                                   # regulares no Python é "." e não "*".
for j in range(len(palavras)):
    if len(padrao) == len(palavras[j]):
        temp.append(palavras[j])

padrao2 = re.compile(padrao2, re.IGNORECASE)   # transformando o padrão de expressão regular em um
                                               # objeto que não faz distinção entre caixa baixa e alta.

resposta = filter(padrao2.match, temp) # Criando uma lista contendo todos os 'matches'.

if resposta == []:
    print "Nenhum resultado encontrado."
else:
    print "As palavras que satisfazem o padrão", padrao, "são:", resposta, "\n"




