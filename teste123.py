# hash
placares = {
    "matheus": 12 + 2 + 4 - 8 - 4 - 8 - 4 + 8 - 8,
    "leticia": 8 + 11 + 14 - 2 + 7 + 11 - 3 - 1 - 3,
    "nata": -2 + 4 - 11 + 3 + 9 - 11 - 4 - 5 + 5,
    "caio": 17 + 10 + 14 + 4 + 16 + 15 - 2 + 11 + 9,
    "rhyas": 0 - 17 + 1 - 17 - 10 + 18 + 13,
    "rafa": 10 - 0 - 0 - 6 - 0 - 5 + 16 + 13 - 6,
    "thais": 8 - 13 - 1 - 16 - 9 + 5 - 13 - 3,
    "vitor": -5 - 7 - 1 + 6
}

# for pra mostrar todos
for nome, placar in placares.items():
    print(f'Placar de {nome} = {placar}')

# maior e menor placar
maior = max(placares.items(), key=lambda x: x[1])
menor = min(placares.items(), key=lambda x: x[1])

print("\n-=-=-=-=--=- Destaques -=-=-=-=--=-")
print(f'Maior placar: {maior[0]} com {maior[1]} pontos')
print(f'Menor placar: {menor[0]} com {menor[1]} pontos')
