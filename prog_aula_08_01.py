#- Faça um programa que solicite o salário bruto de um funcionário para calcular o seu salário líquido,sabendo que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato.

#Entrada de dados
salario_bruto = float(input('informe o seu salario bruto:R$'))

#Processamento de dados
imposto_de_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - imposto_de_renda - sindicato 
print('----DESCONTOS----')
print(f'Imposto de renda (11%): R${imposto_de_renda:.1f})')
print(f'INSS (8%): R${inss:.1f}')
print(f'sindicato(5%): R${sindicato:.1f}')
print(f'seu salario liquido e:{salario_liquido:.1f}')
