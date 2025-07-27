# Leetcde 2488: Count Subarrays With Median K
# https://leetcode.com/problems/count-subarrays-with-median-k/
# Solved on 27th of July, 2025
import collections


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        """
        Counts the number of subarrays where 'k' is the median.

        Args:
            nums (list[int]): The input list of integers.
            k (int): The target median value.
        Returns:
            int: The total count of subarrays where 'k' is the median.
        """
        kIndex = nums.index(k)

        balanceCounts = collections.defaultdict(int)
        balanceCounts[0] = 1

        currentBalance = 0
        for i in range(kIndex - 1, -1, -1):
            if nums[i] > k:
                currentBalance += 1
            else:
                currentBalance -= 1
            balanceCounts[currentBalance] += 1

        totalCount = 0
        currentBalance = 0
        for i in range(kIndex, len(nums)):
            if nums[i] > k:
                currentBalance += 1
            elif nums[i] < k:
                currentBalance -= 1

            neededForZero = -currentBalance
            totalCount += balanceCounts[neededForZero]

            neededForOne = 1 - currentBalance
            totalCount += balanceCounts[neededForOne]

        return totalCount