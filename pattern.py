n=int(input())
for i in range(1,2*n):
    for j in range(1,2*n):
        if i==1 or i==j or i+j==2*n or i==2*n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
