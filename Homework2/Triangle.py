def function_n(n):
    if n > 0:
        print("Acute Triangle")
    if n < 0:
        print("Obtuse Triangle")
    if n == 0:
        print("Right Triangle")

def Triangle(a,b,c):
    if a+b>c and b+c>a and a+c>b:
        if max(a,b,c) == c:
            n = (a**2 + b**2 - c**2) / (2*a*b)
        if max(a,b,c) == b :
            n = (a**2 + c**2 - b**2) / (2*a*c)
        if max(a,b,c) == a :
            n = (b**2 + c**2 - a**2) / (2*b*c)
        function_n(n)
    else:
        print("No Triangle")


def main():
    while True:
        print("Input a")
        a=int(input())
        print("Input b")
        b=int(input())
        print("Input c")
        c=int(input())
        print(Triangle(a,b,c))
        print("**************Would you like again <yes/no>***************")
        answer=input()
        if answer == "no":
            print("*****************Thanks for testing****************")
            break
main()


