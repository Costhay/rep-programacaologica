# Função para limpar as vendas
def limpar_vendas(lista_vendas):
    vendas_validas = []
    
    for valor in lista_vendas:
        if valor > 0 and valor < 10000:
            vendas_validas.append(valor)
    
    return vendas_validas


# Função para analisar os dados
def analisar_dados(lista_limpa):
    total = sum(lista_limpa)
    
    if len(lista_limpa) > 0:
        media = total / len(lista_limpa)
    else:
        media = 0
    
    return (total, media)


# Função para definir o status
def definir_status(media):
    if media > 5000:
        return "Alta Performance"
    elif 2000 <= media <= 5000:
        return "Performance Estável"
    else:
        return "Performance Crítica"

# Identificação da filial
continuar = 1

while continuar == 1:

    nome_filial = input("\nDigite o nome da filial: ")
    vendas = []

    # Coleta de vendas
    while True:
        valor = float(input("Digite o valor da venda (0 para encerrar): "))
        
        if valor == 0:
            break
        
        vendas.append(valor)

    # Tratamento
    vendas_limpas = limpar_vendas(vendas)

    # Processamento
    total, media = analisar_dados(vendas_limpas)

    # Classificação
    status = definir_status(media)

    print("\n" + "=" * 100)
    print(f"RELATÓRIO DA FILIAL: {nome_filial}")
    print("=" * 100)

    print(f"Status de Performance: {status}")
    print(f"Faturamento Total: R$ {total:.2f}")
    print(f"Média das Vendas: R$ {media:.2f}")

    print("\nVendas Válidas:")

    contador = 1
    for venda in vendas_limpas:
        print(f"{contador}. R$ {venda:.2f}")
        contador += 1

    print("=" * 100)

    continuar = int(input("\nDigite 1 para analisar outra filial ou 0 para encerrar: "))

print("=" * 100)
print("\nPrograma encerrado.")
print("=" * 100)