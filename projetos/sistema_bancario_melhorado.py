saldo = 2500
saque = 0
LIMITE_DIARIO = 1500
extrato = ""
usuarios = {}
total_numero_de_contas = 0


def CadastrarUsuario(usuarios):
    print("Olá, bem vindo ao Sistema de Cadastro, por favor siga o passo a passo:")
    
    nome = input("Nome:\n> ")
    dob = input("Data de Nascimento:\n> ")
    cpf = input("CPF:\n> ")

    if cpf in usuarios:
        print(f"Erro! O CPF {cpf} já está cadastrado em nosso sistema.")
        return None

    logradouro = input("Logradouro:\n> ")
    nro = input("Número de Residência:\n> ")
    bairro = input("Bairro:\n> ")
    cidade = input("Cidade:\n> ")
    sigla = input("Sigla do Estado:\n> ")
    contas = []

    endereco = f"{logradouro}, {nro} - {bairro} - {cidade}/{sigla}"

    dados_usuario = {
        "nome": nome,
        "data_nascimento": dob,
        "cpf": cpf,
        "endereco": endereco,
        "contas": contas
    }

    usuarios[cpf] = dados_usuario
    print(f"\nUsuário {nome} cadastrado com sucesso!")
    return dados_usuario


def CadastrarConta(agencia="0001", *, usuario, conta_numero):
    global total_numero_de_contas

    numero_conta = f"{conta_numero + 1:04}"
    conta = {
        "numero_conta": numero_conta,
        "agencia": agencia,
        "usuario": usuario
    }

    usuario["contas"].append(conta)
    total_numero_de_contas += 1

    print(f"Conta número {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")
    return conta

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada até o momento.")
        return

    for conta in contas:
        print(f"""
=================== Conta {conta['numero_conta']} ===================
Agência: {conta['agencia']}
Usuário: {conta['usuario']['nome']}
""")

def Deposito(valor, saldo, /):
    global extrato
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print(f"\nValor depositado com sucesso! R$ {valor}")
    return saldo


def Saque(*, valor, saldo, index):
    global extrato

    if index > LIMITE_DIARIO:
        print("Erro! Você atingiu o limite diário de saque.")
        return saldo, index

    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    print(f"\nValor sacado com sucesso! R$ {valor}")
    return saldo, index


def Extrato(saldo, /, *, extrato):
    print(f"""\nSegue abaixo seu extrato:
================================================================================================
{extrato}
                            O seu saldo atual é: R$ {saldo}
================================================================================================
""")


print("Olá! Bem-vindo ao banco.\n")

# =================== Interface ===================

while True:

    opcao = input("Digite [1] para Entrar com Usuário, [2] para se Cadastrar ou [0] para Sair.\n> ")

    # =================== Opção 1 ===================

    if opcao == "1":
        cpf_input = input("Por favor, insira seu CPF.\n> ")

        if cpf_input in usuarios:
            print(f"Bem-vindo de volta, {usuarios[cpf_input]['nome']}!")
            opcao = input("Digite [1] para Entrar em sua Conta, [2] para Criar outra Conta ou [3] para Listar as Contas já criadas com esse Usuário.\n> ")

            # =================== Opção 1.1 ===================

            if opcao == "1":

                while True:

                    try:
                        
                        opcao = int(input(f"""
+-------------------------------- MENU BANCÁRIO --------------------------------+
|                                                                               |
|   [0] - Sair   |   [1] - Sacar    |    [2] - Depositar   |   [3] - Extrato    |    
|                                                                               |
+-------------------------------------------------------------------------------+

"""))

                        # =================== Opção 1.1.1 ===================

                        if opcao == 1:
                            answer = int(input("Informe a quantidade de dinheiro que quer sacar: R$ "))
                            if answer <= 0:
                                print("Por favor, selecione um número possível!\n")
                            elif answer > saldo:
                                print("Erro! Dinheiro insuficiente, deseja fazer um empréstimo?\n")
                            else:
                                saque += answer
                                saldo, saque = Saque(valor = answer, saldo = saldo, index = saque)

                        # =================== Opção 1.1.2 ===================
                                
                        elif opcao == 2:
                            answer = int(input("Informe a quantidade de dinheiro que quer depositar: R$ "))
                            if answer <= 0:
                                print("Por favor, selecione um número possível!\n")
                            else:
                                saldo = Deposito(answer, saldo)

                        # =================== Opção 1.1.3 ===================

                        elif opcao == 3:
                            Extrato(saldo, extrato = extrato)

                        # =================== Opção 1.1.4 ===================

                        elif opcao == 0:
                            print("\nDesconectando da Conta!")
                            break; 
                        
                        # =================== Opção 1.1.5 ===================

                        else:
                            print("\nErro! Selecione uma opção existente!")
                            continue;
                    
                    # =================== Opção 1.1.6 ===================

                    except:

                        print("\nErro! Digite um número válido.")
                        continue
            
            # =================== Opção 1.2 ===================
            
            elif opcao == "2":
                CadastrarConta(usuario = usuarios[cpf_input], conta_numero = total_numero_de_contas)

            elif opcao == "3":
                listar_contas(usuarios[cpf_input]['contas'])

            # =================== Opção 1.3 ===================

            else:
                print("\nErro! Selecione uma opção existente.")

        else:
            print("\nErro! CPF não encontrado. Deseja se cadastrar?")

    # =================== Opção 2 ===================

    elif opcao == "2":
        CadastrarUsuario(usuarios)

    # =================== Opção 3 ===================

    elif opcao == "0":
        print("\nVolte sempre!")
        break; 

    # =================== Opção 3 ===================

    else:
        print("\nErro! Selecione uma opção existente.")


