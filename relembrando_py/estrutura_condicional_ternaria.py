saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Erro!"

print(f"{status} na operação.")