a=[]
m=int(input('enter number of rows: '))
n=int(input('enter number of columns: '))
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    a.append(row)
for i in range(m):
    for j in range(n):
        print(a[i][j],end='')
    print()
t=0
for i in range(m):
    for j in range(n):
        if i+j==n-1:
            t=t+a[i][j]
print('trace: ',t)
