#- Crie um programa que solicite ao usuário dez números inteiros e os armazene em uma lista. Depois exiba a lista completa, assim como o maior e o menor número da lista. Também mostre a soma e a média de todos os numeros


# Criando e manipulando uma lista
num = [2,4,10,60,70,80,150,160,400,500]
print(num)
print(f'A soma dos valores é {sum(num)}')
print(f'O maior valor encontrado foi {max(num)}')
print(f'O menor valor encontrado foi {min(num)}')
print(f'A quantidade de valores encontrado é {len(num)}')
print(f'A média dos valores é {(sum(num)/len(num)):.1f}')