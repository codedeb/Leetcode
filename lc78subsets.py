def subsets(nums):
    if len(nums) == 0:
        return [[]]
    else:
        sub = subsets(nums[1:])
        res = []
        word = nums[0]
        for i in sub:
            res.append(i)
            res.append(i + [word])

    return res


a = subsets([1, 2, 3])
print(a)
