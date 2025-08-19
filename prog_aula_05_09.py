## - Construa um programa onde serão fornecidas as duas notas de dez alunos. Calcule a média de cada aluno e mostre a situação de cada aluno de acordo com as seguintes condições:
# - Se a média for maior igual a 70 -> ATENDIDO
# - Se a média for maior igual a 30 e menor que 70 -> PARCIALMENTE ATENDIDO
# - Se a média for menor que 30 -> NÃO ATENDIDO

# Entrada dos dados
for i in range(10):
    nome = input('Informe o nome do estudante: ')
    n1 = float(input('Informe a primeira nota de 0 a 100: '))
    n2 = float(input('Informe a segunda nota de 0 a 100: '))
# Processamento dos dados
    media = (n1 + n2) / 2
    if media >= 70:
        sit = 'ATENDIDO'
    elif media >= 30:
        sit = 'PARCIALMENTE ATENDIDO'
    else:
        sit = 'NÃO ATENDIDO'
# Saída dos dados
    print(f'Sr(a) {nome}, a sua média foi {media}, portanto você está {sit}')
print('-- FIM DA EXECUÇÃO --')