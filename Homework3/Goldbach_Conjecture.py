def prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5+1),2):
        if n % i == 0:
            return False
    return True

n=int(input())
if prime(n - 2):
    print(2," ",n-2)
for i in range(3,n//2+1,2):
    if prime(i) and prime(n-i):
        print(i," ",n-i)
        break

