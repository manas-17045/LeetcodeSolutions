# Leetcode 2106: Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
# Solved on 20th of July, 2025
class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        """
        Calculates the maximum number of fruits that can be harvested given a starting position and maximum steps.
        :param fruits: A list of lists, where each inner list contains [position, amount] of fruits.
        :param startPos: The starting position.
        :param k: The maximum number of steps allowed.
        :return: The maximum total number of fruits that can be harvested.
        """
        n = len(fruits)
        if n == 0:
            return 0

        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = prefixSum[i] + fruits[i][1]

        maxFruits = 0
        left = 0
        for right in range(n):
            while left <= right:
                leftPos = fruits[left][0]
                rightPos = fruits[right][0]

                steps = (rightPos - leftPos) + min(abs(startPos - leftPos), abs(startPos - rightPos))

                if steps <= k:
                    break
                else:
                    left += 1

            if left <= right:
                currentFruits = prefixSum[right + 1] - prefixSum[left]
                maxFruits = max(maxFruits, currentFruits)

        return maxFruits