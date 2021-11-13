def Desired_Word(word, pattern):
    if len(set(word)) == len(set(pattern)):
        permutation = {}
        for index, letter in enumerate(word):
            if letter in permutation:
                if permutation[letter] != pattern[index]:
                    return False
            else:
                permutation[letter]=pattern[index]
        return word

def Replace_Pattern(word, pattern):
    a = []
    for w in word:
        if Desired_Word(w,pattern):
            a.append(w)
    print(a)

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
Replace_Pattern(words,pattern)







