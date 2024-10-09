# Break: Uma ferramenta usada para interromper e encerrar um loop

while True:
    
    nome = input('Digite o seu nome ou escreva "sair": ')
    if nome == 'sair':
        break # Para a execução do "while" e sai do loop de repetição
    print(f'Seu nome é {nome}')

print('Programa finalizado.')