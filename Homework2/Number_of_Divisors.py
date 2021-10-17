def Number_of_Divisors(n):
    j=0
    i=n
    while i >= 1: 
        if n % i == 0:
            j=j+1
        i=i-1
    return j

def test_Number_of_Divisors(n , expectedResult):
    print("Testing Number_of_Divisors")
    result = Number_of_Divisors(n)
    if result != expectedResult:
        print("Expected to get",expectedResult,"but got",result)
    else:
        print("Ok")

def main():
    while True:
        print("Input a natural n")
        n=int(input())
        print(Number_of_Divisors(n))
        print(test_Number_of_Divisors(n, Number_of_Divisors(n)))
        print("**************Would you like test <yes/no>***************")
        answer=input()
        if answer == "no":
            print("*****************Thanks for testing****************")
            break
main()

