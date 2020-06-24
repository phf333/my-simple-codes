class Funcionario(object):
    def __init__(self,mat,nome):
        self.mat=mat
        self.nome=nome
        self.vendas= []

    def lancavendas(self,ven):
        self.vendas.append(ven)

    def comissao(self,per=0.1):
        total=sum(self.vendas)
        self.comissao= total * per
        print "total vendido+ ",total
        
class Gerente(Funcionario):
    def __init__(self,mat,nome,per):
        Funcionario.__init__(self,mat,nome)
        self.per=per

    def lancavendas(self,ven):
        print 'Um Gerente nao efetua vendas!'

    def comissao(self,lista_func):
        valor=0

        for func in lista_func:
            valor += func.comissao

        self.comissao= valor * self.per
        print 'total das comissoes dos seus subalternos =', valor
def main():
    fred=Gerente("000","Fred",0.8)    
    maicon=Funcionario("001","Maicon")
    olaf=Funcionario("002","Olaf")

    print '\n', 'Criando lista com os valores semanais das vendas de cada funcionario'
    vendas_maicon= [100.00, 1000.00]
    vendas_olaf= [0,15.00]

    print 'Vendas do funcionario Maicon:', vendas_maicon
    print 'Vendas do funcionario Olaf:', vendas_olaf

    
    print '\n','Adicionando os valores das vendas do funcionario maicon em sua lista de vendas'
    for valor in vendas_maicon:
        maicon.lancavendas(valor)
        print 'valor =', valor, '->', maicon.vendas

    print '\n', 'Adicionando os valores das vendas do funcionario olaf em sua lista de vendas'
    for valor in vendas_olaf:
        olaf.lancavendas(valor)
        print 'valor =', valor, '->', olaf.vendas

    print '\n', 'Calculando comissoes dos funcionarios maicon (10%) e olaf(20%)'
    print 'maicon:'
    maicon.comissao(0.1)
    print 'Comissao  =', maicon.comissao, '\n'
    print 'olaf:'
    olaf.comissao(0.2)
    print 'Comissao olaf =', olaf.comissao, '\n'

    print '\n', 'Calculando comissao do gerente fred'
    fred.comissao([maicon,olaf])
    print 'Comissao fred =', fred.comissao


if __name__ == "__main__":
    main()




    
        
        
        
