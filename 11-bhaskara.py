# Atividdade - Desenvolva um programa que calcula as raízes de uma equação quadrática utilizando a fórmula de Bhaskara

# 1- Solicitando ao usuário que insira os valores dos coeficientes a, b e c
print("Atividade - Algoritmo: Calculadora da Fórmula de Bhaskara\n")
nome = str(input("Digite o seu nome: "))
print(f"Olá, {nome}!")

a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))

while a == 0:
    print("O coeficiente 'A' não pode ser igual a zero; Caso contrário, a equação não é quadrática.")
    print("Digite o valor de A: ")

# 2 - Cálculo do discriminante (delta)
delta = b**2 - 4*a*c

# 3 - Verificando o valor do discriminante (delta)

# 3.1 - Se delta for negativo:
if delta < 0:
    print (f"{nome}, a equação não possui raízes reais.")
# 3.2 - Se delta for igual a zero:
elif delta == 0:
    # Cálculo da única raiz real
    x = -b/(2*a)
    print (f"{nome}, a equação possui uma única raiz real, sendo ela: {x:.2f}")
# 3.3 - Se delta for positivo:
else:
    # Cálculo das duas raízes reais
    x1 = (-b+(delta ** 0.5)/2*a)
    x2 = (-b-(delta ** 0.5)/2*a)
    print (f"{nome}, a equação possui duas raízes reais, sendo elas: {x1:.3f} e {x2:.3f}")