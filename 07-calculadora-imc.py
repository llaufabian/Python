# Atividade - Desenvolver um algoritmo que, a partir da leitura do peso e idade do usuário, calcule o imc.

# Atribuição de variáveis / Formulário

print("Atividade - Algoritmo: Calculadora de IMC")
nome = str(input("Digite o seu nome: "))
print(f"Olá, {nome}!")
peso = int(input("Digite o seu peso (em Kg): "))
altura = float(input("Digite a sua altura (em metro): "))
imc = peso / (altura ** 2)

# Calculadora de IMC

print(f"Seu IMC é {imc:.2f}.")
print("Classificação do IMC: ")
if imc < 18.5:
    print(f"{nome}, seu IMC está em 'Abaixo do peso normal'.")
elif imc >= 18.5 and imc < 25:
    print(f"{nome}, seu IMC está em 'Peso normal'.")
elif imc >= 25 and imc < 30:
    print(f"{nome}, seu IMC está em 'Sobrepeso'.")
elif imc >= 30 and imc < 35:
    print(f"{nome}, seu IMC está em 'Obesidade grau I'.")
elif imc >= 35 and imc < 40:
    print(f"{nome}, seu IMC está em 'Obesidade grau II'.")
else:
    print(f"{nome}, seu IMC está em 'Obesidade grau III'.")