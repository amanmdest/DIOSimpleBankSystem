menu= """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        n = 1
        novo_deposito = float(input("Qual o valor do deposito? ").strip())

        if novo_deposito > 0:
            try:
                saldo += novo_deposito
                extrato += f"Depósito: R$ {novo_deposito:.2f}\n"
                print(f"""
                      Último Depósito: {novo_deposito:.2f}
                      Saldo: {saldo:.2f}
                      """)

            except ValueError:
                print("Valor inválido, tente novamente.")
                break
            
    elif opcao == "s":
        saque = float(input("Qual o valor do saque? ").strip())

        limite_insuficiente = saque > limite
        saldo_insuficiente = saque > saldo
        limite_saques_insuficiente = numero_saques >= LIMITE_SAQUES

        if limite_insuficiente:
            print("Operação falhou! O valor do saque excedeu o limite")
        elif saldo_insuficiente:
            print("Operação falhou! O seu saldo é insuficiente.")
        elif limite_saques_insuficiente:
            print("Operação falhou! Número de saques excedido.")
        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n" 
            numero_saques +1
            print(f"Saque efetuado na conta, seu saldo é de: {saldo:.2f}\n")

        else:
            print("Saque não efetuado. Valor inválido, tente novamente.")    

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada: ", menu)