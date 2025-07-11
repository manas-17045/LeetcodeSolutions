# Leetcode 2281: Sum of Total Strength of Wizards
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/
# Solved on 11th of Juy, 2025
class Solution:
    def totalStrength(self, strength: list[int]) -> int:
        """
        Calculates the total strength of wizards based on their individual strengths.

        The total strength is defined as the sum of (min_val * sum_of_elements) for all possible subarrays.
        This problem can be efficiently solved using a monotonic stack to find the nearest smaller/greater elements
        and prefix sums to calculate subarray sums quickly.

        Args:
            strength: A list of integers representing the strength of each wizard.

        Returns:
            The total strength of wizards modulo 10^9 + 7.
        """
        n = len(strength)
        mod = 10**9 + 7

        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        prefixSum = [0] * (n + 1)
        for i in range(n):
            prefixSum[i + 1] = (prefixSum[i] + strength[i]) % mod

        prefixOfPrefixSum = [0] * (n + 2)
        for i in range(n + 1):
            prefixOfPrefixSum[i + 1] = (prefixOfPrefixSum[i] + prefixSum[i]) % mod

        totalStrength = 0
        for i in range(n):
            leftBound = left[i] + 1
            rightBound = right[i] - 1

            countLeft = i - leftBound + 1
            countRight = rightBound - i + 1

            sumPrefixRight = (prefixOfPrefixSum[rightBound + 2] - prefixOfPrefixSum[i + 1] + mod) % mod
            sumPrefixLeft = (prefixOfPrefixSum[i + 1] - prefixOfPrefixSum[leftBound] + mod) % mod

            positiveTerm = (countLeft * sumPrefixRight) % mod
            negativeTerm = (countRight * sumPrefixLeft) % mod

            sumOfSubarraySums = (positiveTerm - negativeTerm + mod) % mod

            term = (strength[i] * sumOfSubarraySums) % mod
            totalStrength = (totalStrength + term) % mod

        return totalStrength