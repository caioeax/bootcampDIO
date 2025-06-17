conta_normal = True
conta_universitaria = True

saldo = 2000
saque = 2300
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realizado!")
    elif saque <= (saldo + cheque_especial):
        print("saque realizado com cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado")
    else:
        print("saldo insuficiente")