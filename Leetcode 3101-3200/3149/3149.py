# Leetcode 3149: Find the Minimum Cost Array Permutation
# https://leetcode.com/problems/find-the-minimum-cost-array-permutation/
# Solved on 1st of December, 2025
class Solution:
    def findPermutation(self, nums: list[int]) -> list[int]:
        """
        Finds the permutation of indices that minimizes the total cost.
        The cost is defined as the sum of absolute differences between adjacent elements in the permutation,
        plus the absolute difference between the last and first elements.
        :param nums: A list of integers representing the values at each index.
        :return: A list of integers representing the permutation of indices.
        """
        n = len(nums)
        memo = [[-1] * n for _ in range(1 << n)]
        pathChoice = [[-1] * n for _ in range(1 << n)]

        def calculateMinCost(mask, lastIndex):
            if mask == (1 << n) - 1:
                return abs(lastIndex - nums[0])

            if memo[mask][lastIndex] != -1:
                return memo[mask][lastIndex]

            minCost = float('inf')
            bestNode = -1

            for nextIndex in range(n):
                if not (mask & (1 << nextIndex)):
                    currentCost = abs(lastIndex - nums[nextIndex]) + calculateMinCost(mask | (1 << nextIndex),
                                                                                      nextIndex)
                    if currentCost < minCost:
                        minCost = currentCost
                        bestNode = nextIndex

            memo[mask][lastIndex] = minCost
            pathChoice[mask][lastIndex] = bestNode
            return minCost

        calculateMinCost(1, 0)

        resultPermutation = [0]
        currentMask = 1
        currentIndex = 0

        for _ in range(n - 1):
            nextNode = pathChoice[currentMask][currentIndex]
            resultPermutation.append(nextNode)
            currentMask |= (1 << nextNode)
            currentIndex = nextNode

        return resultPermutation