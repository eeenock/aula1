from BancoLib import Banco

print("Bem-vindo")
bancoUfrpe = Banco("UABJ")
print("Menu")
print("0 - Sair")
print("1 - Criar uma Nova Conta")
print("2 - Consultar Saldo Conta")
print("3 - Depositar na Conta")
print("4 - Sacar na Conta")
print("5 - Render Poupanca")
print("6 - Render Bônus")
print ("7 - Consultar Bônus")
escolha = int(input("Digite a opção desejada:"))
while escolha > 0:
    if escolha == 1:
        # criar uma conta
        print("Criando Conta...")
        print("1 - Conta Corrente")
        print("2 - Conta Poupanca")
        print("3 - Conta Bonificada")
        opcao = int(input("digite o tipo da conta:"))
        if opcao == 1:
            numConta = bancoUfrpe.criarConta()
        if opcao == 2:
            numConta = bancoUfrpe.criarPoupanca()
        if opcao == 3:
            numConta = bancoUfrpe.criarContaBonificada()
        print("Conta criada:", numConta)
        
    elif escolha == 2:
        print("Consultando Saldo...")
        numConta = int(input("digite o numero da conta:"))
        resp = bancoUfrpe.consultaSaldo(numConta,valor)
        if resp >= 0:
         print("o saldo da conta", numConta, "é", resp, "R$")
        else :
          print("Esta conta não existe")  
           
    elif escolha == 3:
        print("Depositando Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja depositar:"))
        resp = bancoUfrpe.depositar(numConta, valor)

        if resp == 2 or resp == 1 : 
             print("Valor Depositado")  
        elif resp == -1:
             print("Deposite acima de 0 R$")      
        elif resp == 0 :
             print("Esta conta não existe")


    elif escolha == 4:
        print("Sacando da Conta...")
        numConta = int(input("digite o numero da conta:"))
        valor = int(input("digite o valor que deseja sacar:"))
        resp = bancoUfrpe.sacar(numConta, valor)
        if resp == True:  # significa resp == True
            print("Valor Sacado")
        if resp == -1:
            print("Esta conta não existe")    
        else:
            print("Saldo Insuficiente")

    elif escolha == 5:
        print("Rendendo Poupanca...")
        numConta = int(input("digite o numero da Conta Poupança:"))
        resp = bancoUfrpe.renderPoupanca(numConta)
        if resp == True:
            print("Poupanca com novo saldo")
        if resp == -1 :
            print("Seu saldo é Insuficiente. Você precisa de saldo positivo para render, Deposite!!!")
        if resp == -2 :  
            print("Esta conta não é Poupança")      
        else:
            print("A conta não existe")

    if escolha == 6:
        print("Rendendo Bônus...")
        numConta = int(input("digite o numero da Conta Bonificada:"))
        resp = bancoUfrpe.renderBonus(numConta)
        if resp == True:
            print("Conta Bonificada com novo saldo")
        elif resp == -1:  
            print("Seu bônus é Insuficiente. Para acumular Bônus, Deposite!!!")
        elif resp == -2: 
            print("Esta conta não é Bonificada") 
        else:
            print("A conta não existe")


    if escolha == 7:
        print("Consultando Bônus...")
        numConta = int(input("Digite o numero da conta:"))
        resp = bancoUfrpe.consultaBonus(numConta)
        if resp == -2 :
             print("Esta conta não é do tipo Bonificada!!")
        if resp == -1:
             print ("Esta conta não existe")
        else :
             print("O bônus da conta", numConta, "é", resp, "R$")  


    escolha = int(input("Digite a opção desejada:"))                