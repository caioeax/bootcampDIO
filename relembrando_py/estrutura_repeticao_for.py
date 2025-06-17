# texto = input("Informe um texto: ")
# vogais = "AEIOU"

# for letra in texto:
#     if letra.upper() in vogais:
#         print(letra, end=", ")
# else:
#     print()
#     print("over")


# for numero in range(0, 11):
#     print(numero, end=" ")

# print()
# for numero in range (0, 51, 5):
#     print(numero, end=" ")


for numero in range(61):
    if numero % 5 == 0 and numero % 3 == 0:
        print("FizzBuzz")
    elif numero % 5 == 0:
        print("Fizz")
    elif numero % 3 == 0:
        print("Buzz")
    else:
        print(numero)