def mergesort(nums):
    # recursion
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]

        mergesort(left)  # calling left function recursively
        mergesort(right)  # calling right function recursively

        i = j = k = 0
        while i < len(left) and j < len(right):  # itrating till any side finished
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
                k += 1

            else:
                nums[k] = right[j]
                j += 1
                k += 1
        while i < len(left):  # if  left partition is yet to finish
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):  # if right partition is yet to finish
            nums[k] = right[j]
            j += 1
            k += 1

    return nums  # merging


a = mergesort([4, 1, 2, 6])
print(a)
