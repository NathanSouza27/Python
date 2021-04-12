#Develop a program that reads a student's two grades, calculates and displays his average.

n1 = float(input('Student first note:'))
n2 = float(input('Student second note:'))

m = (n1 +n2) /2

print('The average of {} and {} is equal {:.1f}'.format(n1, n2, m))