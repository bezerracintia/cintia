#- Faça um Programa que peça um número correspondente a um determinado ano e em
#seguida informe se este ano é ou não bissexto.

# Entrada de dados:
ano = int(input('digiteum ano , para saber se o mesmo e bissexto ou não'))

#Saída de dados
if(ano % 4 == 0):
    print(f' o ano {ano}  é bissexto.')
else:
    print(f' o ano{ano}não é bissexto')