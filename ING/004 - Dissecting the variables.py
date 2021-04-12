#Make a program that reads something on the keyboard and shows on the screen its primitive type and all possible informa
# tion about it.

n = input('Type it somenthing:')

print('The primitive type of this value is:',type(n))
print('Only spaces?',n.isspace())
print('It is a numeric?',n.isnumeric()) 
print('It is an alphabetical?',n.isalpha())
print('It is an alphanmeric?',n.isalnum())
print('It is in uppercase?',n.isupper())
print('It is in lowercase?',n.islower())
print('It is capitalized?',n.istitle())