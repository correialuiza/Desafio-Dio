saldo = 1000
limite = 1500
extrato = ""
numero_saque = 0
limite_saque = 3

nome = " BBank"
mensagem = f"""
   Olá seja bem vindo ao BBank ! 
   Para mais detalhes da sua conta clique no menu a baixo:
   """
print(mensagem)


menu = """
      
=============== MENU ===============
      
1 - Depositar
2 - Sacar
3 - Extrato 
4 - Sair     

====================================                  
      
  """   

while True:
    opcao = int(input(menu))


    if opcao == 1:
       valor = float(input("Informe o valor do depósito: "))
       
       if valor > 0:
          saldo += valor   #saldo = saldo + valor
          extrato += f"Depósito: R$ {valor:.2f}\n"

       else :
           print ("Operação falhou! Valor informado é inválido")

    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saque = numero_saque >= limite_saque

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação Falhou! Número máximo de saque exceido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque:R$ {valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! O valor informado é inválido")

    elif opcao == 3:
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == 4:
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



    