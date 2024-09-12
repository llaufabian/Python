# Atividade - Implementar o algoritmo do voto obrigatório em Python, de acordo com o pseudo-código em portugol descrito em sala.

print("Atividade - Algoritmo do Voto Obrigatório")

nome = str(input("Digite o seu nome: "))
idade = int(input("Olá! Digite a sua idade: "))

if idade >=18 and idade < 65:
    print(f"{nome}, seu voto é obrigatório!")
elif idade >= 16 and idade <=17 or idade >= 65:
    print(f"{nome}, seu voto é opcional!")
else:
    print(f"{nome}, seu voto ainda não é permitido!")
