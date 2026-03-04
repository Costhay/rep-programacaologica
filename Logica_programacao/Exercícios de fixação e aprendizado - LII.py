# 1.Integração: Operadores + Condicionais: #
# Exercício: Peça ao usuário seu peso (kg) e altura (m). Calcule o IMC (peso/altura2). #
# Em seguida, utilize uma estrutura if/elif/else para exibir a classificação: #
# • Menor que 18.5: Abaixo do peso
# • Entre 18.5 e 24.9: Peso normal
# • Entre 25.0 e 29.9: Sobrepeso
# • 30.0 ou mais: Obesidade
# Dica: Use operadores de comparação encadeados (ex: 18.5 <= imc < 25).

peso = float(input("Insira o peso: "))

altura = float(input("Insira a altura em cm: "))

imc = peso / altura ** 2

if imc < 18.5:
    print(f"\n O resultado do seu IMC é: {imc:.2f}. \nEsse número indica que você está no peso ideal")
    
elif 18.6 <= imc <= 24.9:
    print(f"\n O resultado do seu IMC é: {imc:.2f}. \nEsse número indica que você está no peso normal")    
    
elif 25.0 <= imc <= 29.9:
    print(f"\n O resultado do seu IMC é: {imc:.2f}. \nEsse número indica que você está com sobrepeso")
    
else:
    print(f"\n O resultado do seu IMC é: {imc:.2f}. \nEsse número indica que você está com obesidade")

# 2.Integração: Repetição FOR + Operadores de Associação: #
# Exercício: Peça para o usuário digitar uma frase ou nome completo. Utilizando um #
# laço for, percorra cada caractere da string e verifique se ele é uma vogal (utilizando #
# o operador in "aeiouAEIOU"). Ao final, exiba o total de vogais encontradas. #

contar_vogais = 0

frase = input("Digite uma frase qualquer:\n")

for caractere in frase:
    if caractere in "aeiouAEIOU":
        contar_vogais += 1
        
print("\n Total de voagais:", contar_vogais)

# 3. Integração: Repetição WHILE + Condicionais + Atribuição:
#Exercício: Crie um programa que inicialize uma variável saldo = 500.0. Exiba um
#menu com as opções: (1) Depositar, (2) Sacar e (3) Sair.
#• Se escolher depositar, peça o valor e some ao saldo.
#• Se escolher sacar, verifique se há saldo suficiente; se sim, subtraia; se não,
#avise "Saldo Insuficiente".
#• O programa deve repetir (while) até que o usuário escolha a opção 3.

saldo = 500.00

while True:
    print("\n OPERAÇÕES:\n (1) Depositar \n (2) Sacar \n (3) Sair \n")
    
    operacao = int(input("Escolha uma opção: "))
    
    if operacao == 1:
         deposito = float(input("\n Qual valor sera depositado hoje?\n"))
         saldo += deposito
         print(f"\n Depósito realizado com sucesso. \n Novo saldo: R$ {saldo:.2f}")
        
    elif operacao == 2:
        while True:
            saque = float(input("\n Digite o valor para sacar: "))
            
            if saque <= saldo:
                saldo -= saque
                print(f"\n Saque realizado com sucesso. \n Saldo atual: R$ {saldo:.2f}")
                break
            else:
                print("\n Saldo insuficiente. \n Refaça a operação")
                
    elif operacao == 3:
        print("\n Encerrando atendimento. \n Obrigada por utilizar nosso serviço.")
        break
    
    #Uma validação para que o usário não escreva 10.
    
    else:
        print("\n Opção inválida. Escolha entre as opções disponíveis no menu")

# 4. Integração: Identidade + Coleções Simples:
# Exercício: Crie uma lista dados_originais = [10, 20, 30].
# 1. Crie dados_referencia = dados_originais.
# 2. Crie dados_copia = [10, 20, 30].
# Use o operador is para mostrar ao aluno que dados_referencia é o mesmo
# objeto que o original, mas dados_copia não é, apesar de terem valores
# idênticos.

dados_originais = [10, 20, 30]
dados_referencia = dados_originais
dados_copia = [10, 20, 30]

print("\n Dados Referencia é o mesmo que Dados originais pois o teste 'IS' retorna:", dados_referencia is dados_originais, ". \n O que siginifica true? \n Que a comparação é verdadeira! \n Porque o segundo foi atribuido como igualdade do primeiro \n")

print("\n Porém Dados Referencia não é o mesmo que Dados Copia, \n apesar dos valores da lista serem exatamente os mesmos, \n pois o teste 'IS' retorna:", dados_referencia is dados_copia, ". \n O que significa False? \n Que a comparação é falsa! \n Porque em dados copia foi atribuido uma lista com valores, \n e não igualdade com dados referencia")
