def Digit_Product(n):
    mul = 1
    while n > 0:
        if n % 10 != 0:
            mul = mul * (n % 10)
        n = n // 10
    return mul

def test_Digit_Product(n , expectedResult):
    print("Testing Digit_Product")
    result = Digit_Product(n)
    if result != expectedResult:
        print("Expected to get",expectedResult,"but got",result)
    else:
        print("Ok")

def main():        
    b=True
    while b:
        print("Input a natural n")
        n=int(input())
        print(Digit_Product(n))
        print(test_Digit_Product(n, Digit_Product(n)))
        print("**************Would you like test <yes/no>***************")
        m=input()
        if m == "no":
            print("*****************Thanks for testing****************")
            b=False
main()




        


