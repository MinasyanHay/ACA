a=int(input("a="))
b=int(input("b="))

for i in range(a,b+1):
    c = str(i)
    if c == c[::-1]:
        print(c, end =" ")

