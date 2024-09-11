# Tipos de Dados Primitivos:
#  - Inteiro (int): Um número inteiro, como 1, 2, 3, etc.
#  - Float (float): Um número real ou decimal, como 3.14 ou -0.5.
#  - String (str): Uma cadeia de caracteres, como "Olá, mundo!" ou "123", usando aspas.
#  - Boolean (bool): Um valor lógico, que pode ser True ou False.
#  - None (NoneType): Um valor especial que representa a ausência de valor.
#  - Complex (complex): Um número complexo, como 3+4j ou 2-5j, com parte real e imaginária.
#  - List (list): Uma lista de valores, como [1, 2, 3] ou ["a", "b", "c"].
#  - Tupla (tuple): Uma coleção imutável e ordenada de valores, como (1, 2, 3) ou ("a", "b", "c").
#  - Dicionário (dict): Uma coleção de elementos, não-ordenados e indexados.

# Atribuição de variável por captura
nome = input("Digite o seu nome: ")
print(type(nome))
idade = input("Digite a sua idade: ")
print(type(idade))
altura = input("Digite a sua altura: ")
print(type(altura))

# Exibir na tela
print(f"nome: {nome} idade: {idade} altura: {altura}")

# Exemplo de conversão de string para inteiro
valorA = int(input("Digite o valor de A: "))
valorB = int(input("Digite o valor de B: "))
resultado = valorA + valorB
print(f"O resultado da soma é: {resultado}")
# Exemplo de conversão de string para float
valorA = float(input("Digite o valor de A: "))
valorB = float(input("Digite o valor de B: "))
resultado = valorA + valorB
print(f"O resultado da soma é: {resultado}")
