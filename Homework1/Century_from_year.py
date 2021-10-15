year = int(input())
if year >= 0:
    century = year // 100
    if year % 100 != 0:
        century += 1;
    print(century)
