# Leetcode 3413: Maximum Coins From K Consecutive Bags
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/
# Solved on 31st of December, 2025
class Solution:
    def maximumCoins(self, coins: list[list[int]], k: int) -> int:
        """
        Calculates the maximum coins that can be collected from k consecutive bags.

        Args:
            coins: A list of lists, where each inner list represents a segment of bags
                   [start_bag_index, end_bag_index, coins_per_bag].
            k: The number of consecutive bags to consider.
        Returns:
            The maximum number of coins that can be collected.
        """
        coins.sort()
        n = len(coins)
        maxCoins = 0

        currentSum = 0
        right = 0
        for i in range(n):
            windowStart = coins[i][0]
            windowEnd = windowStart + k - 1

            while right < n and coins[right][0] <= windowEnd:
                segStart, segEnd, val = coins[right]
                currentSum += (segEnd - segStart + 1) * val
                right += 1

            partialSum = currentSum
            if right > 0:
                lastSegStart, lastSegEnd, lastVal = coins[right - 1]
                if lastSegEnd > windowEnd:
                    partialSum -= (lastSegEnd - windowEnd) * lastVal

            maxCoins = max(maxCoins, partialSum)

            segStart, segEnd, val = coins[i]
            currentSum -= (segEnd - segStart + 1) * val

        currentSum = 0
        left = 0
        for i in range(n):
            segStart, segEnd, val = coins[i]
            currentSum += (segEnd - segStart + 1) * val

            windowEnd = segEnd
            windowStart = windowEnd - k + 1

            while left <= i and coins[left][1] < windowStart:
                lStart, lEnd, lVal = coins[left]
                currentSum -= (lEnd - lStart + 1) * lVal
                left += 1

            partialSum = currentSum
            if left <= i:
                firstSegStart, firstSegEnd, firstVal = coins[left]
                if firstSegStart < windowStart:
                    partialSum -= (windowStart - firstSegStart) * firstVal

            maxCoins = max(maxCoins, partialSum)

        return maxCoins