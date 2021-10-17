def sum(n):
    sum=0
    while n>0:
        sum=sum+n%10
        n=n//10
    return sum

def The_Root_of_the_Number(n):
    print(n)
    if sum(n) >= 10:
        return The_Root_of_the_Number(sum(n))
    else:
        print(sum(n))

def main():
    while True:
        print("Input a natural n")
        n=int(input())
        The_Root_of_the_Number(n)
        print("**************Would you like test <yes/no>***************")
        answer=input()
        if answer == "no":
            print("*****************Thanks for testing****************")
            break
main()
