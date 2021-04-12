#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto

pre = float(input('Qual é o preço do produto? U$ '))

desc = pre * 0.05
total = pre - desc 

print('O produto que custou {}, em promoção com 5% de desconto vai custar U$ {:.2f}'.format(pre,total))