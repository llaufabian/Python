#Contador automático de 1 a 10
#Atividade 08-tabuada.py - Faça um programa que mostre a tabuada de um número que o

contador = 0
multiplicador = int(input("Digite o valor do multiplicador: "))
resultador = 0

while contador <= 10:
    resultado = multiplicador * contador
    print(f"{multiplicador} x {contador} = {resultado}")
    contador += 1