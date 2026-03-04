print("≡" * 100)
prime = """            
         ╭─────────╮
        𓊆│  ◔  ◔   │𓊇
         │    ︶   │
      ╭──┴─────────┴──╮
   𓊆▥▥│  ● ● ● ● ● ●  │▥▥𓊇
      ╰──┬──────────┬─╯
         │   │  │   │
         ╰───╯  ╰───╯      
      """
saudacao = "Seja bem vindo cliente TechInvest! Eu sou o Prime e vou te ajudar em cada etapa"
robo = "ᴘʀɪᴍᴇ, ᴏ ᴀɴᴀʟɪꜱᴛᴀ: "
introducao = """
Nós da TechInvest estamos aqui para entender o seu momento, 
ajuda-lo a mapear seu perfil investidor e 
mostrar onde a organização financeira pode te levar. 
Caso queira, também podemos ajudar com alguma simulações
"""

# Inicio do programa para recepçao do cliente
print(robo)
print(saudacao)
print("≡" * 100)
print(prime)
print("≡" * 100)
print(robo)
print(introducao)
print("≡" * 100)

# Recebimento de dados de entrada do cliente, com validações para evitar valores inválidos
while True:

    nomecliente = input("Insira seu nome e pelo menos um sobrenome: ")

    while " " not in nomecliente:
        print("\nPor favor, insira pelo menos um sobrenome.")
        nomecliente = input("Insira seu nome e pelo menos um sobrenome: ")

    rendacliente = float(input("Informe sua renda liquida: R$ "))

    while rendacliente <= 0:
        print("Por favor inserir um valor válido para o cálculo")
        rendacliente = float(input("Informe sua renda liquida: R$ "))

    gastoscliente = float(input("Informe seus gastos mensais: R$ "))

    while gastoscliente <= 0:
        print("Por favor inserir um valor válido para o cálculo")
        gastoscliente = float(input("Informe seus gastos mensais: R$ "))

    coragemcliente = float(input("Falando de investimentos, atribua um valor de 1 a 10: "))

    while coragemcliente < 1 or coragemcliente > 10:
        print("Por favor, insira um valor entre 1 e 10.")
        coragemcliente = float(input("Falando de investimentos, atribua um valor de 1 a 10: "))

    # Calculos

    saldomensal = rendacliente - gastoscliente
    reserva_seguranca = rendacliente * 6
    falta_reserva = reserva_seguranca - saldomensal

    print(f"""
      Sua renda atual: R$ {rendacliente:,.2f}
      Gastos mensais: R$ {gastoscliente:,.2f}
      Seu estilo de investimento: {coragemcliente}
      
      Saldo mensal atual: R$ {saldomensal:,.2f}
      Reserva de segurança ideal (6x renda): R$ {reserva_seguranca:,.2f}
      Quanto falta para atingir a reserva ideal: R$ {falta_reserva:,.2f}
    """)

    # Confirmacao das informacoes recebidas:
    
    confirmar = input("As informações estão corretas? (S/N): ")

    if confirmar == "S":
        break
    else:
        print("\nVamos inserir os dados novamente.\n")
        print("≡" * 100)

print("≡" * 100)
print(robo)
print(f"Certo! {nomecliente}, vamos para a analise quantitativa do seu cenário atual: ")
print("≡" * 100)

if saldomensal < 0:
    print("\n❰ ALERTA: EMERGÊNCIA FINANCEIRA ❱\n")
    print(f"Seu déficit mensal é de R$ {abs(saldomensal):,.2f}\n")

    opcao = input("Deseja simular um plano para sair do vermelho? Utilize S ou N: ")

    if opcao == "S":

        while True:
            print("""
Como deseja se organizar?
1 - Definir em quantos meses quer sair do vermelho
2 - Definir quanto consegue economizar por mês
0 - Sair da simulação
""")
            escolha = input("Escolha 1, 2 ou 0: ")

            if escolha == "0":
                print("\nEncerrando simulação...\n")
                print("≡" * 100)
                break

            elif escolha == "1":
                meses = int(input("Em quantos meses deseja equilibrar suas finanças? "))

                if meses <= 0:
                    print("Informe um número válido de meses.")
                    continue

                valor_mensal = (abs(saldomensal) / meses) * 1.1

                print(f"\nValor necessário por mês: R$ {valor_mensal:,.2f}")

                if valor_mensal > rendacliente:
                    print("""
⚠ Atenção: Esse valor é maior que sua renda mensal total.
Esse cenário não representa uma condição realista.
Recomendamos revisar o número de meses.
""")

                elif valor_mensal > rendacliente * 0.5:
                    print("""
⚠ Atenção: Esse valor corresponde a mais de 50% da sua renda mensal.
Talvez seja mais adequado optar por definir quanto consegue economizar por mês.
""")

            elif escolha == "2":
                valor = float(input("Quanto consegue economizar por mês? R$ "))

                if valor <= 0:
                    print("Informe um valor válido.")
                    continue

                meses = (abs(saldomensal) / valor) * 1.1

                print(f"""
Você levará aproximadamente {meses:.1f} meses
para sair do vermelho com margem de 10%.
""")

            else:
                print("Opção inválida. Tente novamente.")


else:
    print("❰ Você possui superávit mensal ❱\n")
    print(f"Sobra mensal: R$ {saldomensal:,.2f}\n")

    falta_reserva = reserva_seguranca - saldomensal

    if falta_reserva > 0:
        print(f"Ainda faltam R$ {falta_reserva:,.2f} para atingir sua reserva ideal.\n")
        print("≡" * 100)

        simular = input("Deseja simular um plano para atingir sua reserva? Utilize S ou N: ")

        if simular == "S":

            while True:
                print("""
Como deseja planejar sua reserva?
1 - Definir em quantos meses quer atingir a reserva
2 - Definir quanto consegue guardar por mês
0 - Sair da simulação
""")

                escolha = input("Escolha 1, 2 ou 0: ")

                if escolha == "0":
                    print("\nEncerrando simulação...\n")
                    break

                elif escolha == "1":
                    meses = int(input("Em quantos meses deseja atingir a reserva? "))

                    if meses <= 0:
                        print("Informe um número válido de meses.")
                        continue

                    valor_necessario = falta_reserva / meses

                    print(f"\nValor necessário por mês: R$ {valor_necessario:,.2f}")

                    if valor_necessario > rendacliente:
                        print("""
⚠ Atenção: Esse valor é maior que sua renda mensal total.
Esse cenário não representa uma condição realista.
Recomendamos revisar o número de meses.
""")

                    elif valor_necessario > rendacliente * 0.5:
                        print("""
⚠ Atenção: Esse valor corresponde a mais de 50% da sua renda mensal.
Talvez seja mais adequado optar por definir quanto consegue guardar por mês.
""")

                elif escolha == "2":
                    valor = float(input("Quanto consegue guardar por mês? R$ "))

                    if valor <= 0:
                        print("Informe um valor válido.")
                        continue

                    if valor > rendacliente:
                         renda_extra = valor - rendacliente
                         print(f"""
⚠ Atenção: O valor informado (R$ {valor:,.2f}) é maior que sua renda mensal atual.
Para conseguir guardar esse valor, seria necessário gerar
uma renda extra de aproximadamente R$ {renda_extra:,.2f} por mês.
""")
                         continue
                    
                    meses = falta_reserva / valor

                    print(f"""
Você levará aproximadamente {meses:.1f} meses
para atingir sua reserva ideal.
""")

                else:
                    print("Opção inválida. Tente novamente.")

    else:
        print("🎉 Parabéns! Você já possui estrutura para começar a investir.")
          
#Analise qualitativa
print("")
print("≡" * 100)
print("Agora falando a respeito do seu perfil investidor: ")
print(f"Seu nível de segurança escolhido foi: {coragemcliente}")
print("≡" * 100)

# Perfil conservador até 4

if coragemcliente < 4:
    print("""\nO seu perfil para investimentos é Conservador
Prefere segurança máxima e liquidez.
Recomendado: Tesouro Selic 2027
""")

    simular = input("Deseja simular um investimento? (S/N): ")

    if simular == "S":

        while True:
            anos = int(input("\nPor quantos anos deseja investir? "))
            valor = float(input("Qual valor deseja investir? R$ "))

            if anos <= 0 or valor <= 0:
                print("Informe valores válidos.")
                continue

            # Simulação simples com rendimento estimado 100% SELIC (aprox. 10% ano exemplo)
            taxa = 0.10
            montante = valor * (1 + taxa) ** anos

            print(f"""
Montante bruto estimado após {anos} anos: R$ {montante:,.2f}

Tributação:
Incide Imposto de Renda (22,5% a 15% sobre rendimento).
Investimentos até R$ 10.000 são isentos da taxa de custódia da B3.

Liquidez:
Resgate D+1 (dinheiro no próximo dia útil).
""")

            sair = input("Digite 0 para sair ou qualquer tecla para simular novamente: ")
            if sair == "0":
                break

# Perfil moderado de 4 a 7

elif coragemcliente <= 7:
    print("""\nO seu perfil para investimentos é Moderado
Aceita oscilações para buscar ganhos reais.
Recomendado: Fundos Imobiliários
""")

    simular = input("Deseja simular um investimento? (S/N): ")

    if simular == "S":

        while True:
            anos = int(input("\nPor quantos anos deseja investir? "))
            capital = float(input("Qual valor deseja investir hoje? R$ "))

            if anos <= 0 or capital <= 0:
                print("Informe valores válidos.")
                continue

            # Juros compostos
            taxa = 0.12
            montante = capital * (1 + taxa) ** anos

            print(f"""
Montante estimado após {anos} anos: R$ {montante:,.2f}

Fórmula utilizada:
M = C × (1 + i)^t
Onde:
C = Capital inicial
i = 0,95% por período
t = Tempo
""")

            sair = input("Digite 0 para sair ou qualquer tecla para simular novamente: ")
            if sair == "0":
                break

# Perfil corajoso maior que 7

else:
    print("""\nO seu perfil para investimentos é Arrojado
Confortável com alta volatilidade.
Recomendado: Ações de Tecnologia
""")

    simular = input("Deseja simular uma carteira de ações? (S/N): ")

    if simular == "S":

        print("""
Para simular uma carteira personalizada de ações,
será necessário seguir para o setor especializado da TechInvest.

Já podemos adiantar algumas boas opções do setor:

• Nvidia (NVDA)
• Microsoft (MSFT)
• Alphabet (GOOGL)
• Broadcom (AVGO)

Nosso time de análise avançada poderá montar
uma carteira diversificada conforme seus objetivos.
""")

print("≡" * 100)
print(robo)
print("""Agradecemos pela participação! 
Encerramos as simulações então
Confira nossos outros produtos e simuladores TechInvest
      """)
