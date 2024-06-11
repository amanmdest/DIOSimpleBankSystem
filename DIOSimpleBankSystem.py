import textwrap

def menu():
    menu = """\n
    ================== MENU ==================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\tSair 
    => """
    return input(textwrap.dedent(menu))

def depositar(novo_deposito, saldo, extrato, /):
    if novo_deposito > 0:
        try:
            saldo += novo_deposito
            extrato += f"""Depósito:\t\tR$ {novo_deposito:.2f}
        """
            print(f"""
                    Último Depósito: {novo_deposito:.2f}
                    Saldo: {saldo:.2f}
                    """)
            return saldo, extrato
        except ValueError:
            print("Valor inválido, tente novamente.", menu)

def sacar(*, novo_saque, saldo, extrato, limite, numero_saques, limite_saques):
    limite_insuficiente = novo_saque > limite
    saldo_insuficiente = novo_saque > saldo
    limite_saques_insuficiente = numero_saques >= limite_saques

    if limite_insuficiente:
        print("Operação falhou! O valor do saque excedeu o limite")

    elif saldo_insuficiente:
        print("Operação falhou! O seu saldo é insuficiente.")

    elif limite_saques_insuficiente:
        print("Operação falhou! Número de saques excedido.")

    elif novo_saque > 0:
        saldo -= novo_saque
        extrato += f"Saque:\t\tR$ {novo_saque:.2f}\n"
        numero_saques +1
        print(f"Saque efetuado na conta, seu saldo é de: {saldo:.2f}\n")

    else:
        print("Saque não efetuado. Valor inválido, tente novamente.")    

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print(f"""
        $#$#$#$ EXTRATO $#$#$#$
          
        {"Não foram realizadas movimentações." if not extrato else extrato}
        Saldo: R$ {saldo:.2f}""")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1
  
    while True:
        opcao = menu()

        if opcao == "d":
            novo_deposito = float(input("Qual o valor do deposito? ").strip())
            saldo, extrato = depositar(novo_deposito, saldo, extrato)

        elif opcao == "s":
            novo_saque = float(input("Qual o valor do saque? ").strip())
            saldo, extrato = sacar(
                saldo=saldo,
                novo_saque=novo_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            #numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada: ", menu)

main()