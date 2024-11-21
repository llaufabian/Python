minhalista = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: \n"))
    minhalista.append (numero)

menor = min(minhalista)
maior = max(minhalista)
soma = sum(minhalista)
print(f"\nO menor num. da lista: {menor}\n")
print(f"O maior num. da lista: {maior}\n") 
print(f"A soma dos num. da lista: {soma}\n")

for lista in minhalista:
    print(lista)
