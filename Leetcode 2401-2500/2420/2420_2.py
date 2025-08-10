# Leetcode 2420: Find All Good Indices
# https://leetcode.com/problems/find-all-good-indices/
# Solved on 10th of August, 2025
class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        """
        Finds all "good" indices in a given list of numbers.
        An index `i` is considered "good" if the `k` elements before it are non-increasing
        and the `k` elements after it are non-decreasing.
        :param nums: A list of integers.
        :param k: An integer representing the length of the non-increasing and non-decreasing subarrays.
        :return: A list of good indices.
        """
        n = len(nums)
        if k == 0 or n < 2 * k + 1:
            return []

        nonInc = [1] * n
        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                nonInc[i] = nonInc[i - 1] + 1

        nonDec = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                nonDec[i] = nonDec[i + 1] + 1

        res = []
        # i must have k elements before and after: k <= i < n - k
        for i in range(k, n - k):
            if nonInc[i - 1] >= k and nonDec[i + 1] >= k:
                res.append(i)

        return res