##from math import sqrt
import math

a=input("Digite o valor do coeficiente A: ")
b= input("Digite o valor do coeficiente B: ")
c= input("Digite o valor do coeficiente C: ")
x=(b**2)-(4*a*c)
if x<0:
        print ("Raiz negativa nao pode ser extraida.")
 
else :
    x=math.sqrt(x)
    x1=(-b+x)/(2*a)
    x2=(-b-x)/(2*a)
    print "As raizes sao: ",x1,x2
    print "the end"
    
