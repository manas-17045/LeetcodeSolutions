# Leetcode 2945: Find Maximum Non-decreasing Array Length
# https://leetcode.com/problems/find-maximum-non-decreasing-array-length/
# Solved on 6th of July, 2025
class Solution:
    def findMaximumLength(self, nums: list[int]) -> int:
        """
        Finds the maximum length of a non-decreasing array that can be formed
        by partitioning the input array `nums`.

        The problem asks to partition the array `nums` into `k` subarrays.
        Let the sum of elements in the i-th subarray be `s_i`.
        We want to maximize `k` such that `s_1 <= s_2 <= ... <= s_k`.

        Args:
            nums: A list of integers.

        Returns:
            The maximum number of such subarrays.
        """
        n = len(nums)
        prefixSum = [0] * (n + 1)
        dp = [0] * (n + 1)
        stk = [[0, 0]]

        for i in range(1, n + 1):
            prefixSum[i] = prefixSum[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            low, high = 0, (len(stk) - 1)
            j = 0

            while low <= high:
                mid = (low + high) // 2
                if stk[mid][0] <= prefixSum[i]:
                    j = max(j, mid)
                    low = mid + 1
                else:
                    high = mid - 1

            index = stk[j][1]
            dp[i] = dp[index] + 1
            currLast = 2 * prefixSum[i] - prefixSum[index]

            while stk and stk[-1][0] >= currLast:
                stk.pop()
            stk.append([currLast, i])

        return dp[n]