# Leetcode 3346: Maximum Frequency of an Element After Performing Operations I
# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/
# Solved on 23rd of September, 2025
import bisect


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        """
        This function calculates the maximum frequency of an element in the array `nums`
        such that the difference between any two elements in the subarray is at most `2 * k`,
        and the number of operations used is at most `numOperations`.
        :param nums: A list of integers.
        :param k: An integer representing the maximum allowed difference for a single operation.
        :param numOperations: An integer representing the maximum number of operations allowed.
        :return: An integer representing the maximum frequency.
        """
        nums.sort()
        n = len(nums)

        l = 0
        max_win = 0
        for r in range(n):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            max_win = max(max_win, r - l + 1)

        ans = min(max_win, numOperations)

        i = 0
        while i < n:
            t = nums[i]
            j = i
            while j < n and nums[j] == t:
                j += 1
            count = j - i
            left = bisect.bisect_left(nums, (t - k))
            right = bisect.bisect_right(nums, (t + k)) - 1
            size = right - left + 1 if left <= right else 0
            curr = min(size, (count + numOperations))
            ans = max(ans, curr)
            i = j

        return ans