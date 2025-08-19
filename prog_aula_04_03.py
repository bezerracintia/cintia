#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
#contrataram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
baseado no salário atual:
#- salários até R$ 1280,00 (incluindo) : aumento de 20%
#- salários entre R$ 1280,00 e R$ 2700,00 : aumento de 15%
#- salários entre R$ 2700,00 e R$ 3500,00 : aumento de 10%
#- salários de R$ 3500,00 em diante : aumento de 5%
#Após o aumento ser calculado, informe na tela: o nome do funcionário, assim como o valor do aumento e novo salário

#Entrada de Dados
nome = input('informe o nome do funcionario:')
salário = float(input(' Informe o Salário do funcionário'))

#processamento de dados
if salario <= 1280:
    percentual = 0.20
elif salario > 1280 and salario <=2700:
    percentual = 0.15
elif salario >2700 and salario <=3500:
    percentual =0.10
else:
    perentual = 0.05
    
    #Saída de dados
    print(f' Sr(a) {nome} o seu aumento dserá de R$ {salario = percentual},com isso seu novo salrio serade r${salario + salario = percentual})