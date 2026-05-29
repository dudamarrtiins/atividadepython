senha_correta = "676767"

while True:
    senha_digitada = input("Digite a senha de acesso: ")

    if senha_digitada == senha_correta:
        print("Acesso liberado")
        break
    else:
        print("Senha incorreta! Tente novamente")