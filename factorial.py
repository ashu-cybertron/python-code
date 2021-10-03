#factorial of a number

def cal_factorial(num: int):

    fact=1
    if num<0:
        print("factorial of negative number is not possible")
    elif num==0:
        print('factorial of zero is 1')
    elif num>0:
        for i in range(num,1,-1):
            fact=fact*i
    return fact 

if __name__ == '__main__': 

    print(cal_factorial(4)) 
