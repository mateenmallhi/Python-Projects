# a = int(input('Enter 1st number for addition'))
# b = int(input('Enter 2nd number for addition'))
# c = a + b
# print('Your desired result for addition is:', c)
#
def sum(a = int(input('Enter 1st number for addition : ')), b = int(input('Enter 2nd number for addition : '))):
    c = a + b
    return c
x = sum()
print('Desired result for addition is : ', x)
