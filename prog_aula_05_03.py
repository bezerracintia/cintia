#Criando Estruturas de repetição INFINITAS

print('USANDO O COMANDO WHILE')
resp = 'S'
while resp.upper() == 'S' :
    nome = input('Informe seu Nome')
    resp = input('Deseja informar outro nome (S/N)?')
    print('fim da execução')