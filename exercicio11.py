while True:
    numero = int(input("Digite um número de 1 a 10 para ver sua tabuada: "))
    if 1 <= numero <= 10:
        break
    print("o valor deve estar estritamente entre 1 e 10")

print(f"\n--- Tabuada do {numero} ---")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")