def largestnumber(nums):
    newstr = ''.join(str(i) for i in nums[:: -1])
    print(newstr)


a = largestnumber([3, 30, 34, 5, 9])
print(a)
