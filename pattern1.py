''' print
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''
print("(1)")
print(" ")
rows=5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print(" ")


    ''' print
    1
    2 2
    3 3 3
    4 4 4 4
    5 5 5 5 5'''
print(" ")
print("(2)")
print(" ")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=' ')
    print(" ")

'''print
 1 2 3 4 5
 1 2 3 4
 1 2 3
 1 2
 1 '''
print(" ")
print(" (3)")
print(" ")
for i in range(rows+1,1,-1):
     for j in range(1,i):
         print(j,end=' ')
     print(" ")

'''print
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1'''
print(" ")
print("(4)")
print(" ")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print(" ")



'''print
* * * * *
* * * *
* * *
* *
*
'''
print(" ")
print('(5)')
print(" ")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print('*', end=' ')
    print(' ')
'''print
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1

'''
print(" ")
print('(6)')
print(" ")
for i in range(rows,0,-1):
    for j in range(rows,i-1,-1):
        print(j,end=' ')
    print(" ")





'''print
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15'''
print('(7)')
print(" ")
point=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(point,end= '  ' )
        point=point+1
    print(" ")


'''print
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
print(" ")
print('(8)')
print(" ")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i,end=' ')
        i=(i-1)
    print("\r")

'''
10 9 8 7
6 5 4
3 2
1'''
print(" ")
row=4
num=10
print('(9)')
print(" ")
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(num,end=' ')
        num=num-1
    print("\r")


'''
7 7 7 7 7 7 7
6 6 6 6 6 6
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1'''
print(" ")
row=7
num=7
print('(10)')
print(" ")
for i in range(row,0,-1):
    for j in range(1,i+1):
        print(num,end=' ')

    print("\r")
    num=num-1

'''
print
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5'''
print(" ")
row=5

print('(11)')
print(" ")
for i in range(1,row+1):
    for j in range(i,row+1):
        print(j,end=' ')

    print("\r")
