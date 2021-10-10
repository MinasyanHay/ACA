n = int(input())
lastDigit = n % 10
middleDigit = (n%100) // 10
firstDigit = n // 100
sum = lastDigit + middleDigit + firstDigit
print("Sum =",sum)
