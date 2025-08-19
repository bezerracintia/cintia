#4- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4
#como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente" resposta 0.

# Entrada dos dados
resp = 0
p1 = input('Telefonou para a vítima?(S/N) ')
p2 = input('Esteve no local do crime?(S/N) ')
p3 = input('Mora perto da vítima?(S/N) ')
p4 = input('Devia para a vítima?(S/N) ')
p5 = input('Já trabalhou com a vítima?(S/N) ')

# Processamento dos dados
if p1.upper() == 'S':
    #resp = resp + 1 
    resp += 1
if p2.upper() == 'S':
    resp += 1
if p3.upper() == 'S':
    resp += 1
if p4.upper() == 'S':
    resp += 1
if p5.upper() == 'S':
    resp += 1

# Saída dos dados
if resp == 2:
    print('Você foi classificado(a) como SUSPEITO(A)')
elif resp >= 3 and resp <= 4:
    print('Você foi classificado(a) como CÚMPLICE')
elif resp == 5:
    print('Você foi classificado(a) como ASSASSINO(A)')
else:
    print('Você foi classificado(a) como INOCENTE')