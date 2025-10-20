# Leetcode 2975: Maximum Square Area by Removing Fences From a Field
# https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
# Solved on 20th of October, 2025
class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        """
        Calculates the maximum possible square area that can be formed by selecting two horizontal fences and two vertical fences.

        Args:
            m (int): The total height of the area.
            n (int): The total width of the area.
            hFences (list[int]): A list of integers representing the positions of horizontal fences.
            vFences (list[int]): A list of integers representing the positions of vertical fences.
        Returns:
            int: The maximum square area modulo 10^9 + 7, or -1 if no square can be formed.
        """
        MOD = 10 ** 9 + 7

        h_set = set(hFences)
        v_set = set(vFences)
        h_set.add(1)
        h_set.add(m)
        v_set.add(1)
        v_set.add(n)

        h = sorted(h_set)
        v = sorted(v_set)

        dh = set()
        for i in range(len(h)):
            hi = h[i]
            for j in range(i + 1, len(h)):
                dh.add(h[j] - hi)

        dv = set()
        for i in range(len(v)):
            vi = v[i]
            for j in range(i + 1, len(v)):
                dv.add(v[j] - vi)

        common = dh & dv
        if not common:
            return -1

        max_side = max(common)
        return (max_side * max_side) % MOD