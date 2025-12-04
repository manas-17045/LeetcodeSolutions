# Leetcode 3424: Minimum Cost to Make Arrays Identical
# https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/
# Solved on 4th of November, 2025
class Solution:
    def minCost(self, arr: list[int], brr: list[int], k: int) -> int:
        """
        Calculates the minimum cost to make two arrays identical.

        :param arr: The first input array.
        :param brr: The second input array.
        :param k: The cost to rearrange elements.
        :return: The minimum cost to make the arrays identical.
        """
        directCost = sum(abs(x - y) for x, y in zip(arr, brr))

        arr.sort()
        brr.sort()

        rearrangeCost = k + sum(abs(x - y) for x, y in zip(arr, brr))

        return min(directCost, rearrangeCost)