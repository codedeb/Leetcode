def quicksort(list):
    # recursive
    if len(list) <= 1:  # base case for recursive call
        return list
    else:
        pivot = list.pop()  # Taking last element of the list as pivot

    greaterthanpivot = []  # values greater than pivot
    lesserthanpivot = []  # values smaller than pivot

    for i in list:
        if i < pivot:
            lesserthanpivot.append(i)
        else:
            greaterthanpivot.append(i)

    return quicksort(greaterthanpivot) + [pivot] + quicksort(lesserthanpivot)  # calling recursively


a = quicksort([3, 1, 7, 6])
print(a)
