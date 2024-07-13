
print('Hello this basic Calculator')
print('please select Desired opeation')
print('Enter 1 for Addition : \nEnter 2 for Subtraction : \nEnter 3 for Multiplication : \nEnter 4 for Division :')
m = int(input())
# m = int(input('1 for addition, \n 2 for subtraction, \n 3 for multiplication, \n 4 for division,'))
if m == 1:
        import addition
elif m == 2:
          import subtraction
elif m == 3:
          import multiplication
elif m == 4:
          import division
else:
     print('Invalid command')


