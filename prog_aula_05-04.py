#1- Escreva um programa que, dado 5 números inteiros calcule a soma deles e
#apresente o resultado ao final.

#Entrada de daDOS
soma = 0

#Processamento dos dados
for i in range(5):
    num = int(input('Informe um numero:'))
    soma = soma + num
    print(f'o resultado da soma é {soma}')