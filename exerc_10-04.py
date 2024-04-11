nota = []
soma = 0


while nota != -1:
  nota.append (nota)
soma = soma + nota
media = soma / 10
nota = int(input())
if media >= 7:
  print('Aprovado')
else:
    print('Reprovado')