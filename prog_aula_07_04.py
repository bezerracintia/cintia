#Construa um programa que armazene 10 números inteiros em um vetor. Ao final informe quantos
#números são pares e quantos são ímpares

#Coletando od dados

num = []
par = []
impar = []
for i in range(5):
    num.append(int(input('Informe o Valor: ')))
    if num[i] % 2 == 0:
        par.append(num[i])
    else:
        impar.append(num[i])
print(f'A quantidade de números pares é {len(par)}')
print(par)
print(f'A quantidade de números ímpares é {len(impar)}')
print(impar)