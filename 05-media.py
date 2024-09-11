# Algoritmo Média: criar um algoritmo que leia 4 notas, e apresente uma média final.

print("Algoritmo do cálculo da média")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media  = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média final é: {media:.2f}")  # O :.2f é para mostrar apenas 2 casas decimais