def sums(list, target):
    list.sort()
    l = 0
    r = len(list) - 1
    while l < r:
        if list[l] + list[r] == target:
            return (list[l], list[r])
        elif list[l] + list[r] > target:
            r = r - 1
        else:
            l = l + 1


a = sums([4, 2, 1, 3, 4, 7, 9], 12)

print(a)
