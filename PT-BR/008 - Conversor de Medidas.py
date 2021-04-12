#Escreva um programa que leia um valor em metros e o exima convertido em centímetros a milímetros.

n1 = int(input('Distancia em metros:'))

km = n1 /1000
hm = n1 /100
dam = n1 / 10 
dm = n1 *10
cm = n1 *100
mm = n1 *1000

print('{} Km'.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{} dm'.format(dm))
print('{} cm'.format(cm))
print('{} mm'.format(mm))