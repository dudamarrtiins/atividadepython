
numero = int(input("Digite um número inteiro: "))

# Números menores ou iguais a 1 não são primos
if numero <= 1:
    n_primo = False
else:
    n_primo = True
    # Verifica se existem divisores além de 1 e ele mesmo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            n_primo = False
            break

if n_primo:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo e sim par")