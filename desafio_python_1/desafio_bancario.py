#3 saques
# 500,00
#cuidar do saldo
#não posso deixar negativo

#Extrato listar todos os depositos e saques
#Deve ser no formato 

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[t] Transferencias
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_transferencias = 0
LIMITE_SAQUES = 3
LIMITE_TRANSFERENCIA = 1

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${ valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Você não possui saldo suficiente")

        elif limite_excedido:
            print("O valor do saque excede o limite")

        elif saque_excedido:
            print("Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1

        else:
            print("O valor informado é invalido")



    elif opcao == "e":
        print("\n #####################Extrato#####################")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("##########################################")

    if opcao == "t":
        conta_transferida = int(input("Informe o numero da conta que deseja transferir 111 sem o hifen(-):"))
        valor = float(input("Informe o valor a ser transferido: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        transferencia_excedido = numero_transferencias >= LIMITE_TRANSFERENCIA

        if saldo_excedido:
            print("Você não possui saldo suficiente")

        elif limite_excedido:
            print("O valor do saque excede o limite")

        elif saque_excedido:
            print("Número máximo de transferencias excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Transferências realizada para conta:{conta_transferida} R$ {valor:.2f}\n"
            numero_transferencias +=1

        else:
            print("O valor informado é invalido")


    elif opcao == "q":
        break      

else:
        print("Operação inválida, por favor selecione novamente a operação desejada")