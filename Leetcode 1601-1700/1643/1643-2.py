# Leetcode 1643: Kth Smallest Instructions
# https://leetcode.com/problems/kth-smallest-instructions/
# Solved on 8th of September, 2025
class Solution:
    def kthSmallestPath(self, destination: list[int], k: int) -> str:
        """
        Finds the k-th lexicographically smallest path from (0,0) to a given destination.

        Args:
            destination (list[int]): A list [row, col] representing the destination coordinates.
            k (int): The k-th smallest path to find.

        Returns:
            str: The k-th lexicographically smallest path.
        """
        row, col = destination
        h = col
        v = row
        total = h + v

        C = [[0] * (total + 1) for _ in range(total + 1)]
        for i in range(total + 1):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

        res = []
        for _ in range(total):
            if h == 0:
                res.append('V')
                v -= 1
            elif v == 0:
                res.append('H')
                h -= 1
            else:
                count_starting_with_H = C[h + v - 1][h - 1]
                if count_starting_with_H >= k:
                    res.append('H')
                    h -= 1
                else:
                    res.append('V')
                    k -= count_starting_with_H
                    v -= 1

        return ''.join(res)