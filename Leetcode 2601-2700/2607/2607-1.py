# Leetcode 2607: Make K-Subarray Sums Equal
# https://leetcode.com/problems/make-k-subarray-sums-equal/
# Solved on 30th of September, 2025
import math


class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        """
        Calculates the minimum cost to make all k-subarray sums equal.

        Args:
            arr (list[int]): The input array.
            k (int): The size of the subarrays.
        Returns:
            int: The minimum total cost.
        """
        numElements = len(arr)
        gcdVal = math.gcd(numElements, k)

        totalCost = 0

        for i in range(gcdVal):
            currentGroup = []
            j = i
            while True:
                currentGroup.append(arr[j])
                j = (j + k) % numElements
                if j == i:
                    break

            currentGroup.sort()

            median = currentGroup[len(currentGroup) // 2]

            for num in currentGroup:
                totalCost += abs(num - median)

        return totalCost