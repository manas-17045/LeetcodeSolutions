# Leetcode 2809: Minimum Time t Kae Array Sum At Most x
# https://leetcode.com/problems/minimum-time-to-make-array-sum-at-most-x/
# Solved on 8th of October, 2025
class Solution:
    def minimumTime(self, nums1: list[int], nums2: list[int], x: int) -> int:
        """
        Calculates the minimum time required to make the array sum at most x.
        :param nums1: A list of integers.
        :param nums2: A list of integers.
        :param x: An integer representing the maximum allowed sum.
        :return: The minimum time (an integer) to achieve the sum at most x, or -1 if it's not possible.
        """
        n = len(nums1)
        pairs = sorted(zip(nums2, nums1))

        dp = [0] * (n + 1)

        sumOne = sum(nums1)
        sumTwo = sum(nums2)

        for i in range(n):
            valTwo, valOne = pairs[i]
            for j in range((i + 1), 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + valOne + j * valTwo)

        for t in range(n + 1):
            totalSum = sumOne + t * sumTwo
            if totalSum - dp[t] <= x:
                return t

        return -1