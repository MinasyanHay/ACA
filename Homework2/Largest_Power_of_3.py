def Largest_Power_of_3(n):
    m=1
    while n>=m:
        k=m
        m=m*3
    return k

def test_Largest_Power_of_3(n , expectedResult):
    print("Testing Largest_Power_of_3")
    result = Largest_Power_of_3(n)
    if result != expectedResult:
        print("Expected to get",expectedResult,"but got",result)
    else:
        print("Ok")

def main():
    while True:
        print("Input a natural n")
        n=int(input())
        print(Largest_Power_of_3(n))
        print(test_Largest_Power_of_3(n, Largest_Power_of_3(n)))
        print("**************Would you like test <yes/no>***************")
        answer=input()
        if answer == "no":
            print("*****************Thanks for testing****************")
            break
main()

