# criação do dicionário
tabela_lanchonete = {
    "Salgado": 4.50,
    "Lanche": 6.50,
    "Suco": 3.00,
    "Refrigerante": 3.50,
    "Doce": 1.00
}

print("Dicionário da Lanchonete:")
for produto, preco in tabela_lanchonete.items():
    print(f"{produto}: R$ {preco:.2f}")