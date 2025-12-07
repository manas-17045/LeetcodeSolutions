# Leetcode 2025: Maximum Number of Ways to Partition an Array
# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/
# Solved on 7th of December, 2025
import collections


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:
        """
        Calculates the maximum number of ways to partition an array such that the sum of the left part equals the sum of the right part.

        Args:
            nums: A list of integers representing the array.
            k: An integer that can be used to replace exactly one element in the array.
        Returns:
            The maximum number of ways to partition the array.
        """
        n = len(nums)
        pref = [0] * n
        currentSum = 0
        for i in range(n):
            currentSum += nums[i]
            pref[i] = currentSum

        totalSum = pref[-1]
        rightCounts = collections.Counter(pref[:n - 1])
        leftCounts = collections.Counter()

        maxWays = 0
        if totalSum % 2 == 0:
            maxWays = rightCounts[totalSum // 2]

        for i in range(n):
            diff = k - nums[i]
            newTotal = totalSum + diff

            if newTotal % 2 == 0:
                target = newTotal // 2
                currentWays = leftCounts[target] + rightCounts[target - diff]
                if currentWays > maxWays:
                    maxWays = currentWays

            if i < n - 1:
                val = pref[i]
                rightCounts[val] -= 1
                leftCounts[val] += 1

        return maxWays