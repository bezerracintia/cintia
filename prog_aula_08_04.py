#Foi realizada uma pesquisa de algumas características físicas da população de uma certa região, a
#qual coletaram os seguintes dados referentes a cada habitante para serem analisados:
#- sexo (masculino e feminino)
#- cor dos olhos (azuis, verdes ou castanhos)
# cor dos cabelos (louros, castanhos, pretos)
#- idade
#Faça um programa que determine e escreva:
#a) a maior idade dos habitantes;
#b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
#c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

# Faça um programa que realize uma pesquisa sobre os habitantes de uma determinada cidade. Os dados coletados serão: Nome, Idade, Sexo(M/F). Ao final mostre as seguintes informações:
# - A média das Idades;
# - A quantidade de pessoas do Sexo Masculino e do Sexo Feminino;
# - O nome da pessoa mais nova e mais velha.

# Entrada dos dados

   # - sexo (masculino e feminino)
# - cor dos olhos (azuis, verdes ou castanhos)
# - cor dos cabelos (louros, castanhos, pretos)
# - idade
# Faça um programa que determine e escreva:
# a) a maior idade dos habitantes;
# b) a quantidade de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive;
# c) a quantidade de indivíduos que tenham olhos verdes e cabelos louros;

# Inicialização das variáveis de controle e contadores
maior_idade = 0
qtd_mulheres_18_35 = 0
qtd_olhos_verdes_cabelos_louros = 0
total_habitantes = 0
resposta = 'S'

# Coleta e processamento dos dados
while resposta.upper() == 'S':
    print(f'\n--- Cadastro do {total_habitantes + 1}º Habitante ---')
    sexo = input('Informe o sexo (M/F): ')
    cor_olhos = input('Cor dos olhos (A-Azuis, V-Verdes, C-Castanhos): ')
    cor_cabelos = input('Cor dos cabelos (L-Louros, C-Castanhos, P-Pretos): ')
    idade = int(input('Informe a idade: '))
    total_habitantes += 1

    if idade > maior_idade:
        maior_idade = idade
    if sexo.upper() == 'F' and 18 <= idade <= 35:
        qtd_mulheres_18_35 += 1
    if cor_olhos.upper() == 'V' and cor_cabelos.upper() == 'L':
        qtd_olhos_verdes_cabelos_louros += 1
    resposta = input('\nDeseja cadastrar outro habitante (S/N)? ')

# Exibição dos resultados
if total_habitantes > 0:
    print('\n--- Relatório Final da Pesquisa ---')
    print(f'a) A maior idade dos habitantes é: {maior_idade} anos.')
    print(f'b) Quantidade de mulheres com idade entre 18 e 35 anos: {qtd_mulheres_18_35}.')
    print(f'c) Quantidade de pessoas com olhos verdes e cabelos louros: {qtd_olhos_verdes_cabelos_louros}.')
else:
    print('\nNenhum habitante foi cadastrado.')