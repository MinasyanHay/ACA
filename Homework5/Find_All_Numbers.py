def Find(nums):
    m = []
    for i in range(1,len(nums)+1):
        if i not in nums:
            m.append(i)
    return m


nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Find(nums))
