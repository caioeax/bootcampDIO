nome = "Caio"
idade = 20
profissao = "dev"
linguagem = "py"

pessoa = {"nome": "Caio", "idade": 20, "profissao": "dev", "linguagem": "py"}

print("Olá, me chamo %s, eu tenho %d, trabalho com %s e estou matriculado no curso de %s" % (nome, idade, profissao, linguagem))
print("Olá, me chamo {}, eu tenho {}, trabalho com {} e estou matriculado no curso de {}".format(nome,idade,profissao,linguagem))
print("Olá, me chamo {3}, eu tenho {0}, trabalho com {2} e estou matriculado no curso de {1}".format(idade, linguagem, profissao, nome))
print("Olá, me chamo {nome}, eu tenho {idade}, trabalho com {profissao} e estou matriculado no curso de {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))
print("Olá, me chamo {nome}, eu tenho {idade}, trabalho com {profissao} e estou matriculado no curso de {linguagem}".format(**pessoa))
print(f"Olá, me chamo {nome}, eu tenho {idade}, trabalho com {profissao} e estou matriculado no curso de {linguagem}")

pi = 3.14159

print(f"valor de pi: {pi:.2f}")
print(f"valor de pi: {pi:10.2f}")