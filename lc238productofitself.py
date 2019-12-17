def productExceptSelf(nums):
    left = [1] * len(nums)
    for i in range(1, len(nums)):
        left[i] = left[i-1]*nums[i-1]
    right = [1] * len(nums)
    for i in range(len(nums)-2, -1, -1):
        right[i] = right[i + 1]*nums[i + 1]

    res = [1] * len(nums)
    for i in range(len(res)):
        res[i] = left[i]*right[i]

    return res


a = productExceptSelf([1, 2, 3, 4])
print(a)
