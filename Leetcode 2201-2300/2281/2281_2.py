# Leetcode 2281: Sum of Total Strength of Wizards
# https://leetcode.com/problems/sum-of-total-strength-of-wizards/
# Solved on 11th of Juy, 2025
class Solution:
    def totalStrength(self, strength: list[int]) -> int:
        """
        Calculates the total strength of all possible subarrays.

        The strength of a subarray is defined as the product of its minimum element
        and the sum of all its elements. The total strength is the sum of strengths
        of all subarrays.

        This solution uses a monotonic stack approach to efficiently find the
        contribution of each element as the minimum in various subarrays.
        It leverages prefix sums and prefix of prefix sums to quickly calculate
        the sum of elements within relevant ranges.

        Args:
            strength: A list of integers representing the strength of individual elements.

        Returns:
            An integer representing the total strength of all subarrays, modulo 10^9 + 7.
        """
        MOD = 10 ** 9 + 7
        n = len(strength)

        # Prefix sum and prefix of prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = (prefix[i] + strength[i]) % MOD

        prefix_prefix = [0] * (n + 2)
        for i in range(n + 1):
            prefix_prefix[i + 1] = (prefix_prefix[i] + prefix[i]) % MOD

        # Monotonic stacks to find Previous Less Element (PLE) and Next Less or Equal Element (NLE)
        left = [-1] * n
        right = [n] * n

        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)

        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)

        result = 0
        for i in range(n):
            l = left[i]
            r = right[i]
            total_left = i - l
            total_right = r - i

            # Total contribution from prefix sums
            sum_right = (prefix_prefix[r + 1] - prefix_prefix[i + 1]) * total_left % MOD
            sum_left = (prefix_prefix[i + 1] - prefix_prefix[l + 1]) * total_right % MOD

            contribution = strength[i] * (sum_right - sum_left) % MOD
            result = (result + contribution) % MOD

        return result