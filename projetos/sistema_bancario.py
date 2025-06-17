saldo = 2500
saque = 0
LIMITE_DIARIO = 1500
extrato = ""

def Deposito(valor, saldo):
    global extrato
    saldo += valor

    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"\nValor depositado com sucesso! R$ {valor}")
    return saldo

def Saque(valor, saldo, index):
    global extrato

    if (index) > LIMITE_DIARIO:
        print("Erro! Você atingiu o limite diário de saque.")
        return saldo, index
    
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    print(f"\nValor sacado com sucesso! R$ {valor}")
    return saldo, index

def Extrato(saldo):
    global extrato

    print(f"""\nSegue abaixo seu extrato:
================================================================================================
          
{extrato}
                                O seu saldo atual é: R$ {saldo}
===============================================================================================
""")

while True:

    try:
        
        opcao = int(input(f"""
+-------------------------------- MENU BANCÁRIO --------------------------------+
|                                                                               |
|   [0] - Sair   |   [1] - Sacar    |    [2] - Depositar   |   [3] - Extrato    |    
|                                                                               |
+-------------------------------------------------------------------------------+

"""))

        if opcao == 1:
            answer = int(input("Informe a quantidade de dinheiro que quer sacar: R$ "))
            if answer <= 0:
                print("Por favor, selecione um número possível!\n")
            elif answer > saldo:
                print("Erro! Dinheiro insuficiente, deseja fazer um empréstimo?\n")
            else:
                saque += answer
                saldo, saque = Saque(answer, saldo, saque)
                
        elif opcao == 2:
            answer = int(input("Informe a quantidade de dinheiro que quer depositar: R$ "))
            if answer <= 0:
                print("Por favor, selecione um número possível!\n")
            else:
                saldo = Deposito(answer, saldo)

        elif opcao == 3:
            Extrato(saldo)

        elif opcao == 0:
            print("Volte sempre!")
            break;

        else:
            print("Erro! Selecione uma opção existente!")
            continue;
    
    except:

        print("Erro! Digite um número válido.")
        continue