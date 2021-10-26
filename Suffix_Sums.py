a=[]
n=int(input("How much lenght?"))

for i in range(0,n):
    v=float(input())
    a.append(v)
b=[]
for i in range(0,n):
    sum=0
    for j in range(i,n):
        sum += a[j]
    b.append(sum)

for i in b:
    print(i)

