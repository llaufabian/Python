# Escreva um algoritmo que verifique se um número fornecido pelo usuário é primo
# O programa deve usar um laço 'for' para verificar a divisibilidade do número
# Modo 1
num = int(input("Digite um número: "))
divisivel = 1

# Modo 2
for i in range (2, num + 1):
    if  num % i == 0:
        divisivel += 1

if divisivel == 2:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
