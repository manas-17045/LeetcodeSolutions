# Leetcode 2234: Maximum Total Beauty of the Gardens
# https://leetcode.com/problems/maximum-total-beauty-of-the-gardens/
# Solved on 27th of October, 2025
import bisect


class Solution:
    def maximumBeauty(self, flowers: list[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        """
        Calculates the maximum total beauty of the gardens.

        Args:
            flowers: A list of integers representing the initial number of flowers in each garden.
            newFlowers: An integer representing the number of new flowers available to plant.
            target: An integer representing the target number of flowers for a garden to be considered "full".
            full: An integer representing the beauty gained from a "full" garden.
            partial: An integer representing the beauty gained per flower in a "partial" garden.

        Returns:
            An integer representing the maximum total beauty that can be achieved.
        """
        flowers.sort()

        n = len(flowers)
        incomplete = []
        numAlreadyComplete = 0

        for f in flowers:
            if f >= target:
                numAlreadyComplete += 1
            else:
                incomplete.append(f)

        m = len(incomplete)
        if m == 0:
            return numAlreadyComplete * full

        prefixSum = [0] * (m + 1)
        for i in range(m):
            prefixSum[i + 1] = prefixSum[i] + incomplete[i]

        maxBeauty = 0
        costToComplete = 0

        for i in range(m + 1):
            if i > 0:
                costToComplete += (target - incomplete[m - i])

            if costToComplete > newFlowers:
                break

            flowersLeft = newFlowers - costToComplete
            numComplete = numAlreadyComplete + i

            p = m - i

            minIncomplete = 0
            if p > 0:
                low = 0
                high = target - 1
                bestLevel = 0

                while low <= high:
                    midLevel = (low + high) // 2

                    k = bisect.bisect_left(incomplete, midLevel, 0, p)

                    costToLevel = (midLevel * k) - prefixSum[k]

                    if costToLevel <= flowersLeft:
                        bestLevel = midLevel
                        low = midLevel + 1
                    else:
                        high = midLevel - 1

                minIncomplete = bestLevel

            currentBeauty = (numComplete * full) + (minIncomplete * partial)
            maxBeauty = max(maxBeauty, currentBeauty)

        return maxBeauty