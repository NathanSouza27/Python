# Write a program that asks the number of kilometers traveled by a rental car and the number of days for which it was
# rented. Calculate the price to pay, knowing that the car costs R$ 60 per day and R$ 0.15 per km driven.

dias = int(input('How many days rented? '))
km = int(input('How much km driven? '))

vd = dias * 60
vkm = km * 0.15
valor = vd + vkm 

print('The total to be paid is R$ {:.2f}'.format(valor))