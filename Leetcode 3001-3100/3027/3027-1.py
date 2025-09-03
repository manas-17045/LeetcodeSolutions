# Leetcode 3027: Find the Number of Ways to Place People II
# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/
# Solved on 3rd of September, 2025
class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        """
        Finds the number of ways to place two people (Alice and Bob) such that Alice is at (x1, y1) and Bob is at (x2, y2),
        satisfying x1 <= x2 and y1 >= y2, and there is no other point (x3, y3) such that x1 <= x3 <= x2 and y2 <= y3 <= y1.
        :param points: A list of 2D integer points, where points[i] = [xi, yi].
        :return: The number of valid pairs (Alice, Bob).
        """
        points.sort(key=lambda p: (p[0], -p[1]))
        n = len(points)
        count = 0
        for i in range(n):
            alice = points[i]
            maxY = float('-inf')
            for j in range(i + 1, n):
                bob = points[j]
                if alice[1] >= bob[1]:
                    if bob[1] > maxY:
                        count += 1
                    maxY = max(maxY, bob[1])

        return count