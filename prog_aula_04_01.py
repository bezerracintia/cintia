#- Faça um Programa que pergunte em que turno você estuda. Peça para digitar:
# M- Matutino ou V - Vespertino ou N - Noturno.
#Imprima a mensagem "Bom Dia!","Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso

#entrada de dados
nome = input('informe seu nome:')
turno = input ('digite em que turno você estuda: Use M - mATUTIINO, v - vESPERTINO, n - nOTURNO').UPPER()
if turno == 'M' :
   print('nom , bom dia!')
   
   # Saída de dados
   if turno == 'M':
      print(f'Sr(a) {nome}, Bom Dia!')
   else:
      if turno == 'V':
         print(f'Sr(a) {nome}, Boa Trde!')
      else:
         if turno == 'N' :
            print(f'Sr(a) {nome}, Boa Noite!')
         else:
            print('dados do Turno incorretos!')

