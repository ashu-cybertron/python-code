#factorial of a number
num=eval(input('enter a number'   ))
fact=1
if num<0:
    print("factorial of negative number is not possible")
elif num==0:
    print('factorial of zero is 1')
elif num>0:
 for i in range(num,1,-1):
    fact=fact*i
 print('factorial of',num,'is',fact)
