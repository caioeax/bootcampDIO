saldo = 500

def sacar(valor, saldo):
    if saldo >= valor:
        saldo -= valor
        print(f"Valor sacado! R$ {valor}")
        return saldo

saldo = sacar(100, saldo)
print(saldo)

' OU '

saldo2 = 300

def sacar(valor):
    global saldo2
    if saldo2 >= valor:
        saldo2 -= valor
        print(f"Valor sacado! R$ {valor}")

sacar(100)
print(saldo2)