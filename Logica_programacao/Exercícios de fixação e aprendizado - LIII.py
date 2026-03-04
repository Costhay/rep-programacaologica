saldo_inicial = 1000.00
saldo = saldo_inicial
checkpoint = saldo_inicial

auditor = input("Auditor, insira seu nome para começar: ")

while any(c in "*#$%&@/-+.," for c in auditor):
    print("Nome invalido, por favor não utilize caracteres especiais.\nDigite novamente.\n")
    auditor = input("Auditor, insira seu nome para começar: ")
    print("-" * 60)
    print("Bem vindo auditor, ", auditor)
    print("-" * 60)

for contador in range(4):
    valor = float(input("Digite o valor da transação: R$ "))
    print(f"Transação {contador+1}: R$ {valor}")
    print("-" * 60)
    
    if valor > 500:
        print("Aviso: Transação de alto valor")
        print("-" * 60)
        
    elif valor < 0 and saldo + valor < 0:
        print("Saldo insuficiente. Transação será ignorada")
        print("-" * 60)
    else:
        saldo += valor
    
saldo_final = saldo

print(f"O saldo final é de: R$ {saldo_final}")
print("*" * 60)

if saldo_final is checkpoint:
    print("O saldo final e o checkpoint ainda são o mesmo objeto")
    print("*" * 60)
else:
    print("O saldo final e o checkpoint não são o mesmo objeto")
    print("*" * 60)
