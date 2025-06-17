while True:
    number = int(input("Informe um número: "))

    if number == 10:
        print("over")
        break;

print(f"acertou! o número era: {number}")



for numero in range(100):
    if numero % 2 == 0:
        continue;
    print(numero, end=" ")