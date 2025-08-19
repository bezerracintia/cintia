#Criando um programa 

#Coletando dados 
nomes = []
idades = []
for i in range(5):
    nomes.append(input('informe o nome:'))
    idades.append(int(input('informe a idade:')))
    print('LISTAGEM DOS USUARIOS')
    for i in range(5):
        print(f'{nomes[i]} - {idades[i]}')