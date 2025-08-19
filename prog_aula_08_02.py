#O Departamento Estadual de Meteorologia solicitou o desenvolvimento de um programa que leia um conjunto indeterminado de temperaturas, ao final informe a menor e a maior temperatura, bem como a média delas

#ENTRADA DE DADOS
quantidade = 4
temperatura = []

# Processamentos de dados
for i in range(3):
    temp = float(input(f'Informe a {i+i}'))
    temperatura.append(temp)

    menor = min(temperatura)
    maior = max(temperatura)
    media = sum(temperatura) / len(temperatura)

    print('----RESULTADOS----')
    print(f'Menor temperatura: {menor:.1f}ºc')
    print(f'Maior temperatura: {maior:.1f}ºc')
    print(f'A Média das temperaturas:{media:.1f}')
