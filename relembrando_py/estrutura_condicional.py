MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe sua idade: "))

if idade >= 18:
    print("Pode tirar a CNH.")
else:
    print("Não atingiu a idade legal para retirar a CNH.")


if idade >= MAIOR_IDADE:
    print("pode")
elif idade == IDADE_ESPECIAL:
    print("pode fazer aulas teóricas")
else:
    print("não pode fazer nenhum tipo de aula!")

