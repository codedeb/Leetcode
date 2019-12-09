# Top k frequent elements
from collections import Counter


def topKFrequent(nums, k):
    hashMap = Counter(nums).most_common()

    new = []
    for i in range(k):
        new.append(hashMap[i][0])

    return new


a = topKFrequent([1, 1, 1, 2, 2, 3], 2)

print(a)
