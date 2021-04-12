#Make an algorithm that reads the price of a product and shows its new price with a 5% discount.

pre = float(input('What is the price of the product? U$ '))

desc = pre * 0.05
total = pre - desc 

print('The product that cost {}, on promoption with 5% discont it will cost U$ {:.2f}'.format(pre,total))