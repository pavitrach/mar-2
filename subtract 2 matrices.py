a=[]
m=int(input('enter number of rows: '))
n=int(input('enter number of columns: '))
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    a.append(row)
print(a)
b=[]
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    b.append(row)
print(b)
result=[]
for i in range(m):
    row=[]
    for j in range(n):
        row.append(0)
    result.append(row)
for i in range(m):
    for j in range(n):
        result[i][j]=a[i][j]-b[i][j]
print('resultant matrix: ',result)







        
