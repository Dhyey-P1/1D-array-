cont = True
a= []

while cont == True:
    a.append(int(input('Enter number: ')))
    carry = input('would you like to continue?: ').lower()
    if carry == 'no':
        cont = False

print(a)