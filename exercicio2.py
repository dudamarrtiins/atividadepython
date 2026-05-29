numeros = []
for i in range(3):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

# inicia o maior e o menor com o primeiro número da lista
maior_numero = numeros[0]
menor_numero = numeros[0]

for n in numeros:
    if n > maior_numero:
        maior_numero = n
    if n < menor_numero:
        menor_numero = n

print(f"O maior número digitado foi: {maior_numero}")
print(f"O menor número digitado foi: {menor_numero}")