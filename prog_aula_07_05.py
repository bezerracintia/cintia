#- Faça um programa que verifique a quantidade de acertos de uma prova com cinco questões, sabendo
#que serão fornecidos pelo usuário as letras assinaladas em cada questão. Para isso será criado um vetor chamado
#GABARITO com as seguintes respostas: A, B, B, D, E.

#Coletando os dados
gabarito = ['A','B','B','D','E']
resp = []
q = 1
acertou = 0
for i in range(5):
    resp.append(input(f'informe a letra assinalada na questao{q}:').upper())
    q += 1
    if resp[i] == gabarito [i]:
        acertou += 1
        print(f'----CONFERENCIA----')
        print(gabarito)
        print(resp)
        print(f'voce acertou{acertou}questoes')