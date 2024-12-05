cont = True
a = []

while cont == True:
    a.append(int(input('Enter number: ')))
    carry = input('would you like to continue?: ').lower()
    if carry == 'no':
        cont = False
    elif carry == 'yes':
        cont == True

n = len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)