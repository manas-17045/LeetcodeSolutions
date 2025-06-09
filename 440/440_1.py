# Leetcode 440: K-th Smallest in Lexicographical Order
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# Solved on 9th of June, 2025

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        """
        Finds the k-th smallest number in lexicographical order within the range [1, n].

        Args:
            n: The upper bound of the range (inclusive).
            k: The k-th smallest number to find.

        Returns:
            The k-th smallest number in lexicographical order.
        """
        currentNumber = 1
        k -= 1

        def calculateSteps(n, n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n + 1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps

        while k > 0:
            stepsInSubtree = calculateSteps(n, currentNumber, currentNumber + 1)

            if stepsInSubtree <= k:
                k -= stepsInSubtree
                currentNumber += 1
            else:
                k -= 1
                currentNumber *= 10

        return currentNumber