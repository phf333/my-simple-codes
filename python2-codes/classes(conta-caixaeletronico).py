class Conta():
    def __init__(self,cc,saldo=0):
        self.cc=cc
        self.__saldo=saldo
        
    def AumentarSaldo(self,valor):
        self.__saldo=self.__saldo+valor

    def DiminuirSaldo(self,valor):
        self.__saldo=self.__saldo-valor

    def InfoSaldo(self):
        print self.__saldo

class  Caixa():
    def __init__(self,matr,nome):
        self.matricula=matr
        self.nome=nome

    def EfetuarSaque(self,conta,valor):
        Conta.AumentarSaldo(valor*-1)

    def EfeutarDeposito(self,conta,valor):
        Conta.DiminuirSaldo(valor)

    def ConsultaSaldo(self,conta):
        return Conta.InfoSaldo()

def main():
   conta1=Conta("001")

if __name__ == "__main__":
    main()

