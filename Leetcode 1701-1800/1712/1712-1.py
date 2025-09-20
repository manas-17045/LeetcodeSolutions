# Leetcode 1712: Ways to Split Array Into Three Subarrays
# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
# Solved on 19th of September, 2025
class Solution:
    def waysToSplit(self, nums: list[int]) -> int:
        """
        Calculates the number of ways to split an array into three non-empty subarrays
        such that the sum of the first subarray is less than or equal to the sum of the
        second subarray, and the sum of the second subarray is less than or equal to
        the sum of the third subarray.

        Args:
            nums (list[int]): The input array of non-negative integers.
        Returns:
            int: The number of valid ways to split the array, modulo 10^9 + 7.
        """
        n = len(nums)
        mod = 10**9 + 7

        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + nums[i]

        ans = 0
        leftIndex = 0
        rightIndex = 0

        for i in range(1, (n + 1)):
            leftIndex = max(leftIndex, i + 1)
            while leftIndex < n and prefixSum[leftIndex] < 2 * prefixSum[i]:
                leftIndex += 1

            rightIndex = max(rightIndex, leftIndex)
            while rightIndex < n and 2 * prefixSum[rightIndex] <= prefixSum[n] + prefixSum[i]:
                rightIndex += 1

            if rightIndex > leftIndex:
                ans = (ans + rightIndex - leftIndex) % mod

        return ans