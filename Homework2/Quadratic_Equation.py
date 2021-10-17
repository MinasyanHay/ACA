
def Quadratic_Equation(a,b,c):
    import math
    if(a==0 and b==0 and c==0):
        print("Non-quadratic equation")
        print("No Solutions")
    else:
        if a != 0:
            print("Quadratic equation")
            D=b**2-4*a*c
            print("Discriminant : ",D)
            if D < 0:
                print("No Solutins")
            else:
                if D == 0:
                    x = (-b)/(2*a)
                    print("One Solution : ",x)
                else:
                    x1=(-b+math.sqrt(D))/(2*a)
                    x2=(-b-math.sqrt(D))/(2*a)
                    print("Two Solutions : ", x1 , " and " , x2)
        elif a == 0:
            print("Non-quadratic equation")
            if b == 0:
                print("No Solutions")
            else:
                x=-c/b
                print("One Solution : ", x)

def main():
    
    while True:
        print("Input a ")
        a=float(input())

        print("Input b ")
        b=float(input())

        print("Input c ")
        c=float(input())

        Quadratic_Equation(a,b,c)
        print("**************Would you like test <yes/no>***************")
        answer=input()
        if answer == "no":
            print("*****************Thanks for testing****************")
            break
main()

