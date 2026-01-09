# Leetcode 3795: Minimum Subarray Length With Distinct Sum At Least K
# https://leetcode.com/problems/minimum-subarray-length-with-distinct-sum-at-least-k/
# Solved on 9th of January, 2026
class Solution:
    def minLength(self, nums: list[int], k: int) -> int:
        """
        Finds the minimum length of a subarray such that the sum of its distinct elements is at least k.

        Args:
            nums: A list of integers.
            k: The target sum for distinct elements.

        Returns:
            The minimum length of such a subarray, or -1 if no such subarray exists.
        """
        n = len(nums)
        start = 0
        currentSum = 0
        minLen = float('inf')
        numCounts = {}

        for end in range(n):
            currentNum = nums[end]
            numCounts[currentNum] = numCounts.get(currentNum, 0) + 1

            if numCounts[currentNum] == 1:
                currentSum += currentNum

            while currentSum >= k:
                length = end - start + 1
                if length < minLen:
                    minLen = length

                startNum = nums[start]
                numCounts[startNum] -= 1
                if numCounts[startNum] == 0:
                    currentSum -= startNum
                start += 1

        return minLen if minLen != float('inf') else -1