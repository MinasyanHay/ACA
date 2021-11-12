def power_String(s, n):
    if n < -1:
        if s[:(abs(n)+1)] * abs(n) == s:
            print (s[:(abs(n)+1)])
        else:
            print("undefined")
    else:
        print (s*abs(n))



s = input()
n = int(input())
power_String(s,n)
