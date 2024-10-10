# Desenvolva um programa que converta temperaturas entre as escalas Celsius, Fahreinheit e Kelvin.
# O programa deve apresentar um menu recursivo, no qual o usuário poderá selecionar a opção desejada.
# Após a seleção, o programa solicitará a entrada da temperatura e exibirá o valor convertido.

def exibirMenu():
    print("CONVERSOR DE ESCALAS TERMOMÉTRICAS!\n")
    print("Menu de escolha:")
    print("1. Converter Fahreinheit para Kelvin")
    print("2. Converter Fahreinheit para Celsius")
    print("3. Converter Kelvin para Fahreinheit")
    print("4. Converter Kelvin para Celsius")
    print("5. Converter Celsius para Fahreinheit")
    print("6. Converter Celsius  para Kelvin")
    print("7. Sair")
    escolha = int(input("\nEscolha uma opção: "))
    return escolha

# Declarção de variáveis
opcao = 0
temperatura = 0
Fahr = 0
Kel = 0
Cel = 0

# Início do Código
def Fahr_Kel(Fahr, Kel):
    return (Kel == (Fahr - 32) * 5/9 + 273.15)
def Fahr_Cel(Fahr, Cel):
    return (Cel == (Fahr - 32 * 5/9))
def Kel_Fahr(Kel, Fahr):
    return (Fahr == (Kel - 273.15) * 9/5 + 32)
def Kel_Cel(Kel, Cel):
    return (Cel == Kel - 273.25)
def Cel_Fahr(Cel, Fahr):
    return (Fahr == Cel * 9/5 + 32)
def Cel_Kel(Cel, Kel):
    return (Kel == Cel + 273.15)

while opcao !=7:
    opcao = exibirMenu()
    if opcao in [1, 2]:
        Fahr = float(input("Insira a temperatura em Fahreinheit: "))
    if opcao in [3, 4]:
        Kel = float(input("Insira a temperatura em Kelvin: "))
    if opcao in [5, 6]:
        Cel = float(input("Insira a temperatura em Celsius: "))
    if opcao == 1:
        print(f"A conversão é {Kel == Fahr_Kel(Fahr, Kel)}\n")
    elif opcao == 2:
        print(f"A subtração dos valores é: {Cel == Fahr_Cel(Fahr, Cel)}\n")
    elif opcao == 3:
        print(f"A multiplicação dos valores é: {Kel_Fahr(Kel, Fahr)}\n")
    elif opcao == 4:
        print(f"A divisão dos valores é: {Kel_Cel(Kel, Cel)}\n")
    elif opcao == 5:
        print(f"O resto da divisão dos valores é: {Cel_Fahr(Cel, Fahr)}\n")
    elif opcao == 6:
        print(f"O resto da divisão dos valores é: {Cel_Kel(Cel, Kel)}\n")
    elif opcao == 7:
        print("Finalizando o programa!")
    else:
        print("Opção inválida. Tente novamente.\n")