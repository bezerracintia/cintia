#Faça um programa que pergunte a uma pessoa , asua idade, o seu peso e quanto dormiunas 24 hs e diga se ela 


#Entrada de dados 
idade = int(input('informe sua idade:'))
peso = float(input('informe seu peso:'))
sono = int(input('informe a quantidade de horas de sono'))

#Saída de dados 
if (idade >= 16 and idade <= 69) and (peso >=50) and (sono >= 6):
print( 'você está APTO a doar')
else:
print ('infelizmente você esta INAPTO para doar porque não dormiu o suficiente')
else:
print('infelizmente você está INAPTO para doar porque não possui peso o suficiente')
else:
print('infelizmente você está INAPTO para doar porque não possui IDADEo suficiente')

