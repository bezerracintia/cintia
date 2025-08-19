#3- Utilizando a estrutura do programa anterior, identifique a idade da pessoa mais velha

#Entrada de dados 
soma = 0
idade_mais_velha = 0
nome_mais_velha = 0


    #Entrada de daDOS
soma = 0

#Processamento dos dados
for i in range(10):
    nome = input('Informe seu nome: ')
    idade = int (input('informe a sua idade:'))
  if idade>maior:
    maior = idade
    soma = soma + idade
    #Saída de dados
    média = soma / (i+1)
    print(f'A soma das idades foi {soma}anos')
    print(f'A média das idades foi{média:.1f}anos')
    print('a idade da pessoa mais velha e {maior} anos')