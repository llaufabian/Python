# Desenvolva um programa que controla a exibição de uma sequência de números
# O programa utiliza estrutuas de repetição e controle de fluxo, de acordo com as instruções abaixo:
# 1. O programa deve contar de 1 a 100
# 2. Ao encontrar o número 6, exiba a menssagem "Não vou mostrar o 6" e pule a exibição do número
# 3. Para os números de 10 a 27, exiba a mensagem "Não vou mostrar o [numero]", onde [numero] representa o valor do contador, e também pule a exibição desses números
# 4. Ao chegar no número 40, o programa deve encerrar o loop, sem continuar até o 100
# 5. Após o loop, exiba "Acabou" ou outra mensagem de finalização.

print("\nALGORITMO - CONTROLE DE FLUXO NUMÉRICO!\n")

contador = 0
while contador < 100:
    contador += 1 # (1)

    # Verifica se o valor de 'contador' é 6, para não exibi-lo
    if contador == 6:
        print("Não vou mostrar o 6")
        continue # (2)
    if contador >=10 and contador <= 27:
        print(f"Não vou mostrar o {contador}")
        continue # (3)
    print(contador)
    if contador >= 40:
        break # (4)
# Após o término do loop, imprime a mensagem de finalização
print("\nFim do Programa.") # (5)