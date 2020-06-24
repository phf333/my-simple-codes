# -*- coding: cp1252 -*-
import random

resposta = raw_input("Digite s para iniciar o jogo:")
score= 0
chute=0
while resposta == "s":
    inicial = random.randint(1,100)
    final = random.randint(100,1000)
    sorteado = random.randint(inicial,final)
    print "Adivinhe o numero entre",inicial,"e",final
    min = inicial
    max= final
    print sorteado
    #chute = input("Digite um numero: ")
    while chute != sorteado:
        chute=0
        chute = input("Digite um numero: ")
        if chute > max or chute < min:
            print "Pense bem, meu bom, teu chute está fora do range"
            score=score+1
        else:
            if chute > sorteado:
                print "Seu chute foi maior que o sorteado"
                max= chute - 1
                score=score+1
            elif chute < sorteado:
                print "Seu chute foi menor que o sorteado"
                min = chute + 1
                score=score+1
            else:
                print "Parabéns, você acertou!", "Tentativas: ",score
                print 
    resposta = raw_input("Digite s para continuar...")

