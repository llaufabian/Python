# Continue : Ferramenta usada para interromper o loop, dando continudade ao mesmo.

print("\nCONTADOR DE MÚLTIPLOS!\n")

contador = 0
while contador < 40:
    contador += 1

    # Verifica se o valor de 'contador' é múltiplo de 4
    if (contador % 4 == 0):
        print(f"{contador} é múltiplo!") # Se o número for múltiplo de 4, indica tal com uma mensagem ao lado do mesmo.
        continue # Interrompe a interação atual e volta para o início

    # Se o número não for múltiplo de 4, imprime o valor do contador
    print(contador)
# Após o término do loop, imprime a mensagem de finalizaçãp
print("Fim do Programa.")

print("\nCONTADOR DE MÚLTIPLOS! (V2)\n")

contador = 0
numero = int(input("Digite o número: "))
while contador < (numero*10):
    contador += 1

    # Verifica se o valor de 'contador' é múltiplo de 4
    if (contador % numero == 0):
        print(f"{contador} é múltiplo de {numero}!") # Se o número for múltiplo de 4, indica tal com uma mensagem ao lado do mesmo.
        continue # Interrompe a interação atual e volta para o início

    # Se o número não for múltiplo de 4, imprime o valor do contador
    print(contador)
# Após o término do loop, imprime a mensagem de finalizaçãp
print("Fim do Programa.")