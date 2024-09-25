# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e a quantos anos ele já fuma.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.
# Exiba o total em dias.

# Variáveis
cigpdia = int(input("Quantos cigarros por dia você fuma? "))
anosf = float(input("Há quantos anos você fuma? "))
rel_em_min = (anosf*365*cigpdia*10)
rel_em_dia = rel_em_min / (24*60)
input(f"Sua vida foi reduzida em {rel_em_dia:.2f} dias.")