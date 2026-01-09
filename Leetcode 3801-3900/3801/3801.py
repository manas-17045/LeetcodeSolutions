# Leetcode 3801: Minimum Cost to Merge Sorted Lists
# https://leetcode.com/problems/minimum-cost-to-merge-sorted-lists/
# Solved on 9th of January, 2026
class Solution:
    def minMergeCost(self, lists: list[list[int]]) -> int:
        """
        Calculates the minimum cost to merge a given set of sorted lists.

        Args:
            lists: A list of sorted lists of integers.
        Returns:
            The minimum cost to merge all the lists into a single sorted list.
        """
        n = len(lists)
        limit = 1 << n
        dp = [float('inf')] * limit
        medians = [0] * limit

        for mask in range(1, limit):
            currentElements = []
            for i in range(n):
                if (mask >> i) & 1:
                    currentElements.extend(lists[i])

            currentElements.sort()
            currentLength = len(currentElements)
            medians[mask] = currentElements[(currentLength - 1) // 2]

            if (mask & (mask - 1)) == 0:
                dp[mask] = 0
                continue

            lowestBit = mask & -mask
            subsetMask = mask ^ lowestBit
            sub = subsetMask
            minCost = float('inf')

            while True:
                part1 = sub | lowestBit
                part2 = mask ^ part1

                if part2 > 0:
                    currentMergeCost = dp[part1] + dp[part2] + abs(medians[part1] - medians[part2])
                    if currentMergeCost < minCost:
                        minCost = currentMergeCost

                if sub == 0:
                    break
                sub = (sub - 1) & subsetMask

            dp[mask] = minCost + currentLength

        return dp[limit - 1]