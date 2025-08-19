#Faça um programa que realize uma pesquisa sobre os habitantes de uma
#determinada cidade. Os dados coletados serão: Nome, Idade, Sexo(M/F). Ao final mostre as
#seguintes informações:
#- A média das Idades;
#- A quantidade de pessoas do Sexo Masculino e do Sexo Feminino;
#- O nome da pessoa mais nova e mais velha

#Entrada de dados
resp = 'S'
maior_idade = 0
menor_idade = 500
soma_idade = 0
qtd_m = 0
qtd_f = 0
i = 0
while resp.upper() == 'S':
    nome = input('Informe o Nome: ')
    idade = int(input('Informe a Idade: '))
    sexo = input('Informe o Sexo M p/ Masculino e F p/ Feminino: ')
    soma_idade = soma_idade + idade
    if idade >= maior_idade:
        maior_idade = idade
        nome_maior = nome
    if idade <= menor_idade:
        menor_idade = idade
        nome_menor = nome
    if sexo.upper() == 'M':
        qtd_m += 1
    elif sexo.upper() == 'F':
        qtd_f += 1
    else:
        print('Dados Incorretos')
    i += 1
    resp = input('Deseja Continuar(S/N)? ')
media_idade = soma_idade / i
print(f'A média das idades dos habitantes é {media_idade} anos.')
print(f'Sr(a) {nome_menor}, você tem {menor_idade} anos, portanto é o habitante mais novo da cidade.')
print(f'Sr(a) {nome_maior}, você tem {maior_idade} anos, portanto é o habitante mais antigo da cidade.')
print(f'A quantidade de pessoas do sexo Feminino é {qtd_f} e a quantidade de pessoas do sexo Masculino é {qtd_m}')