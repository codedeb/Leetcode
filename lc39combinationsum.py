def combinationSum(candidates, target):
    arr = []
    candidates = sorted(candidates)

    for i in range(len(candidates)):
        if candidates[i] == target:
            arr.append([candidates[i]])
        elif candidates[i] > target:
            break
        else:
            result = combinationSum(candidates[i:], target-candidates[i])
            for r in result:
                r.append(candidates[i])
                arr.append(r)

    return arr


a = combinationSum([2, 3, 6, 7, 8], 7)
print(a)
