import random


class Conta():
    def __init__(self, numConta):
        self.numero = numConta
        self.saldo = 0

    def deposite(self, valor):
        desconto = valor * 0.001 
        self.saldo = self.saldo + valor - desconto

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo = self.saldo - valor
            return True
        else:
            return False


class Poupanca(Conta):

    def render(self):
        self.saldo = self.saldo + self.saldo*0.001

class contaBonificada(Conta) :

    def render(self):
          self.saldo = self.saldo + self.bonus
          self.bonus = 0 


class Banco():
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def getNome(self):
        return self.nome

    def criarConta(self):
        num = random.randint(0, 1000)
        c = Conta(num)
        self.contas.append(c)
        return num

    def criarPoupanca(self):
        num = random.randint(0, 1000)
        p = Poupanca(num)
        self.contas.append(p)
        return num

    def criarContaBonificada(self):
        num = random.randint(0, 1000)
        cB = contaBonificada(num)
        self.contas.append(cB)
        cB.bonus = 0
        return num

    def buscaConta(self,numConta):
        existente = 0
        conta = 0
        for i in self.contas:
            if i.numero == numConta :
               conta = i
               existente = 1

        if existente == 1 :
           return [True , conta]       
        else:
          return [False, conta]
     
    def consultaSaldo(self, numConta):
        resultadoBusca = self.buscaConta(numConta)
        conta = resultadoBusca[1]
        verifica = resultadoBusca[0]  
        if verifica == True: #caso a conta exista, consulta o saldo
                return conta.saldo
        else:
            return -1 #caso a conta não exista

    def depositar(self, numConta, valor):
        resultadoBusca = self.buscaConta(numConta)
        conta = resultadoBusca[1]
        verifica = resultadoBusca [0]  
        if verifica == True and (not isinstance(conta,contaBonificada)) and valor > 0: # caso a conta exista e nao seja bonificada
           conta.deposite(valor)
           return 2  
        elif verifica == True and isinstance(conta,contaBonificada) and valor > 0: # caso a conta seja bonificada
            conta.deposite(valor)
            conta.bonus = valor * 0.0001 
            return 1 
        elif valor <= 0: #caso insira 0 ou algo negativo no valor do deposito
            return -1       
        elif verifica == False:
         return 0        #caso a conta nao exista
        
    def sacar(self, numConta, valor):
        resultadoBusca = self.buscaConta(numConta)
        conta = resultadoBusca[1]
        verifica = resultadoBusca [0]  

        if verifica == True:
            return conta.sacar(valor)
        else:
            return -1     #conta nao existe

    def renderPoupanca(self, numConta):
        resultadoBusca = self.buscaConta(numConta)
        conta = resultadoBusca[1]
        verifica = resultadoBusca [0] 

        if verifica == False and conta == 0:#caso está conta não exista 
                return False    
        elif verifica == True and isinstance(conta, Poupanca) and conta.saldo > 0:#Caso consigo render a poupanca
                conta.render()
                return True 
        elif  verifica == True and isinstance(conta,Poupanca) and conta.saldo == 0:   #caso a conta exista mas o saldo seja insuficiente  
                return -1      
        else:#caso a conta nao seja poupança
                return -2 

    def renderBonus(self, numConta):
        resultadoBusca = self.buscaConta(numConta)
        conta = resultadoBusca[1]
        verifica = resultadoBusca [0] 

        if verifica == False and conta == 0: #caso está conta não exista 
                return False 
        elif  verifica == True and isinstance(conta,contaBonificada) and conta.bonus == 0 :#caso a conta exista mas o bonus seja insuficiente  
                print(conta.bonus) 
                return -1
        elif verifica == True and isinstance(conta, contaBonificada) and conta.bonus > 0: #caso consiga render o bonus
                conta.render()
                return True    
        else: #caso a conta nao seja Bonificada
                return -2 

    def consultaBonus(self, numConta):
        resultadoBusca = self.buscaConta(numConta)
        conta = resultadoBusca[1]
        verifica = resultadoBusca [0]  
        if verifica == True and isinstance(conta, contaBonificada): #caso consiga consultar o bonus
                return conta.bonus 
        if verifica == False: #caso a conta nao exista
                return -1       
        return -2     #caso a conta exista mas nao seja do tipo bonificada           




