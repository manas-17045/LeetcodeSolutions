# Leetcode 2333: Minimum Sum of Squared Difference
# https://leetcode.com/problems/minimum-sum-of-squared-difference/
# Solved on 23rd of August, 2025
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        """
        Calculates the minimum sum of squared differences between two arrays after performing at most k1 + k2 operations.

        Args:
            nums1 (list[int]): The first input list of integers.
            nums2 (list[int]): The second input list of integers.
            k1 (int): The maximum number of operations allowed for nums1.
            k2 (int): The maximum number of operations allowed for nums2.
        Returns:
            int: The minimum possible sum of squared differences.
        """
        totalK = k1 + k2
        n = len(nums1)

        # Max possible difference is 10^5
        counts = [0] * 100001
        maxDiff = 0
        sumOfDiffs = 0

        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            counts[diff] += 1
            maxDiff = max(maxDiff, diff)
            sumOfDiffs += diff

        if sumOfDiffs <= totalK:
            return 0

        for d in range(maxDiff, 0, -1):
            if counts[d] > 0:
                numToChange = min(counts[d], totalK)

                counts[d] -= numToChange
                counts[d - 1] += numToChange

                totalK -= numToChange

                if totalK == 0:
                    break

        result = 0
        for d in range(1, maxDiff + 1):
            if counts[d] > 0:
                result += counts[d] * (d * d)

        return result