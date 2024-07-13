# g = int(input('Enter 1st number for multiplication'))
# h = int(input('Enter 2nd number for multiplication'))
# i = g * h
# print('Your desired result for multiplication is:', i)

def mul(a = float(input('Enter 1st number for multiplication : ')), b = float(input('Enter 2nd number for Multiplicaton : '))):
    c = a * b
    return c
x = mul()
print('Desired result for multiplication is : ', x)