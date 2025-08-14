# Leetcode 2197: Replace Non-Coprime Numbers in Array
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
# Solved on 14th of August, 2025
from math import gcd


class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        """
        Replaces non-coprime adjacent numbers in a list with their least common multiple (LCM).

        :param nums: A list of integers.
        :return: A list of integers where non-coprime adjacent numbers have been replaced by their LCM.
        """

        stack: list[int] = []

        for num in nums:
            cur = num
            # Keep merging while there is a previous number and gcd > 1
            while stack:
                g = gcd(stack[-1], cur)
                if g == 1:
                    break
                prev = stack.pop()
                # Compute LCM in integer safe way
                cur = (prev // g) * cur
            stack.append(cur)

        return stack