# Atividade 09 "Rent-car": Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
# Assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

# Variáveis
qkm = float(input("Quantos km foram percorridos? "))
qdias = int(input("Durante quantos dias o carro foi alugado? "))

# Cálculo do preço total
total = (qdias*60) + (qkm*0,15)
print(f"O valor total a pagar é R${total:.2f}")