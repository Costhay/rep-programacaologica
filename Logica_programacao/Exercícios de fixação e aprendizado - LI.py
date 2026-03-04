# Exercício 1: Peça ao usuário dois números inteiros. Calcule e exiba a soma, a
# diferença, o produto, a divisão real, a divisão inteira e o resto da divisão
# (módulo) entre eles.

x1 = int(input("Insira um numero inteiro: "))
x2 = int(input("Insira mais um numero inteiro para o calculo: "))

soma = x1 + x2
diferenca = x1 - x2
produto = x1 * x2
divisaoreal = x1 / x2
divisaoint = x1 // x2
resto = x1 % x2

print(f"Os resultados sao:\n \nSoma: {soma}, \nDiferenca: {diferenca}, \nProduto: {produto}, \nDivisao real: {divisaoreal:.2f}, \nDivisao inteira: {divisaoint:.2f} \ne Resto: {resto}")


# Exercício 2: Crie uma variável saldo com valor inicial de 1000. 
# Utilize operadores de atribuição composta (como +=, -=, *=) para simular três
# operações: um depósito de 500, um saque de 200 e um rendimento que
# dobra o saldo atual. Exiba o resultado final.

saldo = 1000.00
print(f"Saldo inicial: R$ {saldo:.2f}")

saldo += 500.00
print(f"Após depósito de R$ 500: R$ {saldo:.2f}")

saldo -= 200.00
print(f"Após saque de R$ 200: R$ {saldo:.2f}")

saldo *= 2
print(f"Após rendimento (saldo dobrado): R$ {saldo:.2f}")

print(f"\nSaldo final: R$ {saldo:.2f}")

# Exercício 3: Receba dois valores numéricos e retorne uma série de
# booleanos (True ou False) verificando se o primeiro é maior que o segundo,
# se são iguais e se o primeiro é diferente do segundo.

num1 = int(input("Insira um valor: "))
num2 = int(input("Insira mais um valor: "))

print("\nVamos comparar os números!\n \nLegenda\n \nFalse: Falso ou seja, o teste não é verdadeiro \nTrue: O teste é verdadeiro\n")

print("O primeiro numero é maior que o segundo?", (num1 > num2))
print("O primeiro numero é igual ao segundo?", (num1 == num2))
print("O primeiro numero é dierente do segundo?", (num1 != num2))

# Exercício 4: Um aluno só é aprovado se tiver presenca maior ou igual a
# 75 E media maior ou igual a 7.0. Receba esses dois valores e verifique se o
# aluno foi aprovado utilizando operadores lógicos.

nota = float(input("Insira a nota: "))
presenca = int(input("Insira a presenca: "))

print("\nO aluno será aprovado mediante:\n \nPresença >= 75%\n Nota >= 7.0\n")
print("Legenda:\n False: o teste indica que uma das duas condições não foi atingida,\nportanto o aluno reprovou!\n \n True: o teste valida que as duas condições foram atingidas,\nportanto o aluno passou\n")
print("Analisando os valores inseridos, o resultado é:", nota >= 7.0 and presenca >= 75)

# Exercício 5: Crie duas listas com os mesmos elementos, por exemplo: a = [1,
# 2] e b = [1, 2]. Crie uma terceira variável c = a. Use o operador de identidade
# para verificar se a é o mesmo objeto que b e se a é o mesmo objeto que c.

a = [1,2]
b = [1,2]
c = a 

print("\n a é o mesmo que b, pois o teste 'IS' retorna:", a is c, "\n O que siginifica true? \n Que a comparação é verdadeira! \n Porque o segundo foi atribuido como igualdade do primeiro \n")
 
print("\n Porém a não é o mesmo que c, \n apesar dos valores da lista serem exatamente os mesmos, \n pois o teste 'IS' retorna:", a is b, "\n O que significa False? \n Que a comparação é falsa! \n Porque em a foi atribuido uma lista com valores, \n e não igualdade com c")

# Exercício 6: Dada a string "Ciência de Dados", verifique se o
# caractere "D" está presente na frase e se a palavra "Python" não está
# presente.

frase = "Ciência de Dados"

print("Consideremos a frase: Ciência de Dados\n True como: A comparação é verdadeira e\n False: A comparação é falsa\n")
print("A letra 'D' está na frase?", "D" in frase)
print("\nA palavra 'Python' NÃO está na frase?", "Python" not in frase)

# Exercício 7: Desenvolva um programa que receba a idade de um nadador e
# classifique-o em uma das seguintes categorias:
#• Infantil: 5 a 12 anos;
#• Juvenil: 13 a 17 anos;
#• Adulto: 18 anos ou mais;
#• Inválido: Menor que 5 anos.

idade = int(input("Qual idade do nadador? "))

if 5 <= idade <= 12:
    print("\nClassificação: Infantil (5 a 12 anos)")
    
elif 13 <= idade <= 17:
    print("\nClassificação: Juvenil (13 a 17 anos)")
        
elif idade <= 18:
    print("\nClassificação: Adulto (maior de 18 anos)")
    
else:
    print("\nClassificação: Inválido (menor que 5 anos)")

# Exercício 8: Peça um número inteiro ao usuário e exiba a tabuada de
# multiplicação desse número de 1 a 10 utilizando o laço for e a
# função range().

num = int(input("Insira um número para ver a tabuada de 1 a 10 dele: "))

for i in range(1, 11):    print(f"\n{num} x {i} = {num * i}")

# Exercício 9: Escreva um programa que peça ao usuário para digitar uma
# senha. O programa deve continuar pedindo a senha (repetição) até que o
# valor digitado seja igual a "python123". Quando acertar, exiba "Acesso
# Permitido".

senha = input("Insira a senha: ")

while senha != "python123":
    print("\nSenha incorreta. \nTente novamente.")
    senha = input("\nInsira a senha: ")

print("\nAcesso liberado!")
