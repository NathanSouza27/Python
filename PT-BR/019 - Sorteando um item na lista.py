#Um professor quer sortear um dos seus quatros alunos para apagar o quadro.Faça um programa que ajude ele,lendo o nome
# deles e escrevendo o nome do escolhido.

import random

pa = str(input('Primeiro aluno: '))
sa = str(input('Segundo aluno: '))
ta = str(input('Terceiro aluno: '))
qa = str(input('Quarto aluno: '))

lista = [pa,sa,ta,qa]
res = random.choice(lista)

print('{}'.format(res))

