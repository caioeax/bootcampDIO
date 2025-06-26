def saudacao():
    print("Olá! Seja bem-vindo!")


def criar_usuario(nome, idade, /, cidade="São Paulo", *, email=None):
    return {
        "nome": nome,
        "idade": idade,
        "cidade": cidade,
        "email": email
    }

usuario = criar_usuario("Caio", 20, email="caio@email.com")
print(usuario)