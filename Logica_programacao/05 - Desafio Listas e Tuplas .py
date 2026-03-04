print("≡" * 150)
vendas_brutas = [(101, "Monitor", 5, 1200.0),(102, "Mouse", 50, 80.0),(103, "Teclado", 8, 150.0),(104, "Case", 3, 50.0)]
print("Lista inicial:\n",vendas_brutas)

estoque_baixo = []
for produto in vendas_brutas:
    if produto[2] < 10:
        estoque_baixo.append(produto)

print("\nProdutos com estoque baixo:\n",estoque_baixo)

inventario = 0
for produto in vendas_brutas:
    inventario += produto[2] * produto[3]

print(f"\nValor total do inventário: R$ {inventario:.2f}")
print("≡" * 150) 

taxa = 1.10
reajuste = []

for produto in vendas_brutas:
    reajuste.append((produto[0], produto[1], produto[2], produto[3] * taxa))

print("\nLista reajustada:\n",reajuste)

novo_inventario = 0
for produto in reajuste:
    novo_inventario += produto[2] * produto[3]

print(f"\nO reajuste foi de {taxa:.2f}% no valor do produto")

print(f"\nNovo valor total do inventário: R$ {novo_inventario:.2f}")
print("≡" * 150) 
