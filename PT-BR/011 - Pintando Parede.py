#Faça um program que leia a altura e a largura de uma parede em metros,calcule a sua área e a quantidade
#de tinta necessária para pintá-la,sabendo que cada litro de tinta pinta uma área de 2m2.

lar = float(input('Largura da parede:'))
comp = float(input('Altura da parede:'))

m2 = lar * comp 
li = m2 / 2

print('Sua parede tem dimensão de {} x {} e sua área é de {} m²'.format(lar, comp,m2))
print('Para pintar essa parede, voce precisará de {}L de tinta'.format(li))