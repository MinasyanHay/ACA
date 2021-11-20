def Keyboard(words):
    f = set("qwertyuiopQWERTYUIOP")
    s = set("asdfghjklASDFGHJKL")
    t = set("zxcvbnmZXCVBNM")
    m = []
    for v in words:

        g = set(list(v))
        if g & f == g:
            m.append(v)
        elif  g & s == g:
            m.append(v)
        elif  g & t == g:
            m.append(v)
    return m

words = ["Hello","Alaska","Dad","Peace"]
print(Keyboard(words))

