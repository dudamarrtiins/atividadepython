#nome
while True:
    nome = input("Digite o nome (maior que 3 caracteres): ").strip()
    if len(nome) > 3:
        break

# Idade
while True:
    idade = int(input("Digite a idade (entre 0 e 150): "))
    if idade >= 0 and idade <= 150:
        break

# Salário
while True:
    salario = float(input("Digite o salário (maior que zero): "))
    if salario > 0:
        break

# Sexo
while True:
    sexo = input("Digite o sexo ('f' ou 'm'): ").lower()
    if sexo in "fm" and len(sexo) == 1:
        break

# Estado Civil
while True:
    estado_civil = input("Digite o estado civil ('s', 'c', 'v', 'd'): ").lower()
    if estado_civil in "scvd" and len(estado_civil) == 1:
        break

print("\nTodos os dados foram validados com sucesso!")