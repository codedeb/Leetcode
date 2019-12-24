def arraysum(nums, target):
    output = []
    for i in range(len(nums)):
        output.append(nums[i])
        while sum(output) > target:
            output.pop(0)

        if sum(output) == target:
            return output
    return None


a = arraysum([1, 2, 3, 4, 5, 6], 12)
print(a)
