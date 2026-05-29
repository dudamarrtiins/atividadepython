L = [5, 7, 2, 9, 4, 1, 3]

tamanho = 0
for elemento in L:
    tamanho += 1

maior = L[0]
menor = L[0]
soma = 0

for elemento in L:
    if elemento > maior:
        maior = elemento
    if elemento < menor:
        menor = elemento
    soma += elemento

print(f"a) tamanho da lista: {tamanho}")
print(f"b) maior valor da lista: {maior}")
print(f"c) menor valor da lista: {menor}")
print(f"d) soma de todos os elementos: {soma}")

lista_crescente = L.copy()
lista_crescente.sort()
print(f"e) lista em ordem crescente: {lista_crescente}")

lista_decrescente = L.copy()
lista_decrescente.sort(reverse=True)
print(f"f) lista em ordem decrescente: {lista_decrescente}")