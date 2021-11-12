def Jewels(Jewels, stones):
    sum = 0
    for char in stones:
        if char in Jewels:
            sum += 1
    print(sum)

Jewels("z","ZZ")

