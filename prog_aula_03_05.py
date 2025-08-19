#Escreva um programa que, dados 3 n´meros inteiros (n1, n2 e n3), diga  qual deles é maior:

#Entrada dos dados 
n1 = int(input('Informe o primeiro valor:')) 
n2 = int(input('Informe o segundo valor:'))    
n3 = int(input('informe o terceiro valor;' ))

# Saída de dados
if n1 > n2 and n1 > n3:
print(f'o número{n1} é o maior valor')
else:
if n2 > n1 and n2 > n3:
    print (f'o número {n2} é o maior valor )'
           else:
           if n3> n1 and n3 > n2:
           print(f'o numero{n3} é o maior valor ')
           else:
           print('verifique os valores informados')