nome = input("Digite um nome: ").upper()

# o len conta as letras
# o range cria os índices
for i in range(1, len(nome) + 1):
    print(nome[:i])