def longest_increasingSubsequence(nums):
    dp = [1]*len(nums)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i] and dp[i] + 1 > dp[j]:
                dp[j] = dp[i] + 1

    return max(dp)


a = longest_increasingSubsequence([1, 0, 2, 3, 5, 4])
print(a)
