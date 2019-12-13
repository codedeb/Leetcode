def permutations(nums):
    if len(nums) == 1:
        return [nums]

    else:
        perm = permutations(nums[1:])
        result = []
        start = nums[0]

        for word in perm:
            for i in range(len(word) + 1):
                result.append(word[:i] + [start] + word[i:])

    return result


a = permutations([1, 2, 3])
print(a)
