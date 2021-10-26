N=int(input())
K=int(input())

a=[]
for i in range(N):
    a.append(int(input()))

b=a.copy()
for i in range(N):
    b[(i+K) % N] = a[i]
print(b)
