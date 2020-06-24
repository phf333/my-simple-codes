class Fibonacci():
    
    def TamanhoSequencia(self):
        self.valor=input("Digite o numero total de valores que queria obter pela sequencia de Fibonacci: ")

    def CriandoFibo(self):
        self.a, self.b = 0, 1
        while self.b < self.valor:
           print self.b
           self.a, self.b = self.b, self.a+self.b

def main():
    a=Fibonacci()
    a.TamanhoSequencia()
    a.CriandoFibo()

if __name__ == "__main__":
    main()
                         
            
      
            
            
            
        

