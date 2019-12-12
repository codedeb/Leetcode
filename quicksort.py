def quicksort(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list.pop()

    greaterthanpivot = []
    lesserthanpivot = []

    for i in list:
        if i < pivot:
            lesserthanpivot.append(i)
        else:
            greaterthanpivot.append(i)

    return quicksort(lesserthanpivot) + [pivot] + quicksort(greaterthanpivot)


a = quicksort([3, 1, 7, 6])
print(a)
