#- Utilizando apenas o conceito de repetição, faça um programa para ler 2 valores e
#se o segundo valor informado for ZERO, deve ser lido um novo valor, pois o segundo valor
#não pode ser igual a zero. Ao final imprimir o resultado da divisão do primeiro valor pelo

#Entrada dos dados
n1 = float(input('informe o primeiro valor'))
while True:
    n2 = float(input('informe o segundo valor '))
    if n2 != 0:
        print(f'o resultado da divisao foi {n1/n2}')
        break
    else:
        print('informe um valor diferentede zero')