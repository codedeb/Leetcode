def subsets(nums):
    if len(nums) == 0:# recursive base case
        return [[]]
    else:
        sub = subsets(nums[1:]) # spliting into subproblems
        res = []
        word = nums[0]
        for i in sub:
            res.append(i)
            res.append(i + [word])

    return res


a = subsets([1, 2, 3])
print(a)
