#Make a program that reads the height and width of a wall in meters, calculate its area and the amount of paint needed
# to paint it, knowing that each liter of paint paints an area of de 2m2.

lar = float(input('Wall width:'))
comp = float(input('Wall length:'))

m2 = lar * comp 
li = m2 / 2

print('You wall has the dimension of {} x {} and your area is {} m²'.format(lar, comp,m2))
print('To paint this wall, you will need {}L of ink'.format(li))