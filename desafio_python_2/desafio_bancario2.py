import textwrap

def menu():
    menu = """\n
    ------------MENU------------

    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [t]\t Transferencias
    [nc]\t Nova Conta
    [lc]\t Listar contas
    [nu]\t Novo usuário
    [q]\t Sair

    => """
    return input(textwrap.dedent(menu))


def depositar(saldo,valor,extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f"Deposito:\t R${ valor:.2f}\n"
            print("=== Depósito realizado com sucesso!===")
        else:
            print("\n@@@Operação falhou! O valor informado é inválido! @@@")

        return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não possui saldo suficiente")

    elif excedeu_limite:
        print("O valor do saque excede o limite")

    elif excedeu_saques:
        print("Número máximo de saques excedido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque\t\t: R$ {valor:.2f}\n"
        numero_saques +=1
        print("=== Saque realizado com sucesso!===")

    else:
        print("O valor informado é invalido")

    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n #####################Extrato#####################")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\naldo: \t\tR$ {saldo:.2f}")
    print("##########################################")


def realizar_transferencia(*,conta_transferida, saldo, valor, extrato, limite,numero_transferencias, limite_transferencia):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_transferencia = numero_transferencias >= limite_transferencia

    if excedeu_saldo:
        print("Você não possui saldo suficiente")

    elif excedeu_limite:
        print("O valor do saque excede o limite")

    elif excedeu_transferencia:
        print("Número máximo de transferencias excedido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Transferências realizada para conta:{conta_transferida} R$ {valor:.2f}\n"
        numero_transferencias +=1

    else:
        print("O valor informado é invalido")

    return saldo,extrato

def criar_usuario(usuarios):
    cpf = input("Informe o CPF(somente números) :")
    usuario = filtrar_usuario(cpf,usuarios)

    if(usuario):
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereceo (logradouro, nro - bairro - cidade/sigla estado):" )

    usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereço":endereco})

    print("=== Usuário criado com sucesso! ===")



def filtrar_usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso!===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}

    print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha  = f"""\

            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            """
        print("="* 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    LIMITE_TRANSFERENCIA = 1
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    numero_transferencias=0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "t":
            conta_transferida = int(input("Informe o numero da conta que deseja transferir 111 sem o hifen(-):"))
            valor = float(input("Informe o valor a ser transferido: "))
            realizar_transferencia(
                conta_transferida=conta_transferida,
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_transferencias=numero_transferencias,
                limite_transferencia=LIMITE_TRANSFERENCIA,
              
            )


        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
