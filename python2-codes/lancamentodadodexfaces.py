import random
lados= input("Digite a quantidade de lados do seu dado, para ser simulado o lancamento: ")  


while True:

    lancamento=input("Voce quer jogar o dado novamente? (DIGITE 1 CASO SIM): ")

    if lancamento == 1:
       print random.randint(1,lados)
    else:
        print "Obrigado"
        break


 




