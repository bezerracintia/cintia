#2- Faça um programa que receba do usuário o nome e a idade de 10 pessoas. Ao final
#mostre a soma e a média das idades

#Entrada de daDOS
soma = 0

#Processamento dos dados
for i in range(10):
    nome = input('Informe seu nome: ')
    idade = int (input('informe a sua idade:'))
    soma = soma + idade
    #Saída de dados
    média = soma / (i+1)
    print(f'A soma das idades foi {soma}anos')
    print(f'A média das idades foi{média:.1f}anos')