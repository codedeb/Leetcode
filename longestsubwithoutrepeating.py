def longestsubs(string):
    hashMap = {}
    start = 0
    maxlen = 0

    for i in range(len(string)):
        if string[i] in hashMap:
            while string[i] in hashMap:
                del hashMap[start[i]]
                start += 1
        hashMap[string[i]] = 0
        maxlen = max(maxlen, i-start + 1)
    return maxlen
