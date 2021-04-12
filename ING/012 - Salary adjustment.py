#Make an algorithm that reads an employee's salary and shows his new salary with a 15% increase.

sal = float(input('What is the employees salary? U$ '))

aum = sal * 0.15
total = sal + aum 

print('An employee who earned {}, with 15% of increase, starts receiving U$ {:.2f}'.format(sal, total))