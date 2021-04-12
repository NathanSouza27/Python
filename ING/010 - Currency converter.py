#Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.
# Consider 1U$ = R$ 3,27.

mon = float(input('How much money do you have in your wallet? U$ '))

con = mon * 3.27

print('With U$ {} you can buy R$ {:.2f}'.format(mon, con))