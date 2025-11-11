# Leetcode 2866: Beautiful Towers II
# https://leetcode.com/problems/beautiful-towers-ii/
# Solved on 11th of November, 2025
class Solution:
    def maximumSumOfHeights(self, maxHeights: list[int]) -> int:
        """
        Calculates the maximum possible sum of heights of a "beautiful tower"
        that can be formed from the given `maxHeights`.

        A beautiful tower is defined such that its heights are non-increasing
        from the peak to the left and non-increasing from the peak to the right.

        Args:
            maxHeights: A list of integers representing the maximum allowed height
                        for each position in the tower.

        Returns:
            An integer representing the maximum possible sum of heights.
        """
        n = len(maxHeights)

        leftSum = [0] * n
        stack = []
        currentSum = 0
        for i in range(n):
            currentHeight = maxHeights[i]
            count = 1
            while stack and stack[-1][0] > currentHeight:
                val, c = stack.pop()
                currentSum -= val * c
                count += c
            currentSum += currentHeight * count
            stack.append((currentHeight, count))
            leftSum[i] = currentSum

        rightSum = [0] * n
        stack = []
        currentSum = 0
        for i in range(n - 1, -1, -1):
            currentHeight = maxHeights[i]
            count = 1
            while stack and stack[-1][0] > currentHeight:
                val, c = stack.pop()
                currentSum -= val * c
                count += c
            currentSum += currentHeight * count
            stack.append((currentHeight, count))
            rightSum[i] = currentSum

        maxTotalSum = 0
        for i in range(n):
            totalSum = leftSum[i] + rightSum[i] - maxHeights[i]
            maxTotalSum = max(maxTotalSum, totalSum)

        return maxTotalSum