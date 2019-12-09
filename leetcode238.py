import numpy


def productExceptSelf(nums):
    newlist = []
    total = numpy.prod(nums)
    for i in range(len(nums)):
        newlist.append(total//nums[i])

    return newlist


a = productExceptSelf([1, 2, 3, 4])
print(a)
