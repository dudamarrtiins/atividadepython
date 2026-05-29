# quantidade de termos da sequência
n = int(input("Digite a quantidade de termos da série de Fibonacci: "))

termo_atual = 1
termo_anterior = 0

if n <= 0:
    print("Por favor, insira um número maior que 0.")
elif n == 1:
    print("Série de Fibonacci: 1")
else:
    print("Série de Fibonacci:")

    print(termo_atual, end="")

    for _ in range(1, n):
        proximo_termo = termo_atual + termo_anterior
        print(f", {proximo_termo}", end="")

        # atualiza as avariáveis para o próximo ciclo
        termo_anterior = termo_atual
        termo_atual = proximo_termo
    print()