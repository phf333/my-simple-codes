from Tkinter import *
import math
import time
import random
    
def iniciar():
    while True:
        showball()
    
    
def clique(event):
    print event.x, event.y

def desenhaBola(x1, y1, x2, y2, queCor, queTag):
    
    mapa.create_oval(x1, y1, x2, y2, \
                     fill=queCor,tags='bola')


def showball():
    x = 0
    diametro = 40
    while (x + diametro) < 800:
        R = 255
        G = 0
        B = 255
        desenhaBola(x, 300 , \
                    x + diametro, 300 + diametro, \
                    '#%02x%02x%02x' % (R,G,B),'bola')
        x+=9
        y=300
        time.sleep(0.016667)
        mapa.update()
        mapa.delete('bola')

    while x > 0:
        R = 255
        G = 0
        B = 255
        desenhaBola(x, 300 , \
                    x + diametro, 300 + diametro, \
                    '#%02x%02x%02x' % (R,G,B),'bola')
        x-=9
        y=300
        time.sleep(0.096667)
        mapa.update()
        mapa.delete('bola')

    

    
#INTERFACE PRINCIPAL
root=Tk()
root.title('Showball')
options=Frame(root,bg='white')
options.pack(fill='x',expand=True)
botao1=Button(options,text='GO!',command=iniciar)
botao1.pack(side='left',fill='x',expand=True)

mapa=Canvas(root,width=800,height=600)
mapa.pack()
mapa.bind("<ButtonRelease-1>", clique)
mainloop()

