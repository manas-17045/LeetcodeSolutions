# Leetcode 1643: Kth Smallest Instructions
# https://leetcode.com/problems/kth-smallest-instructions/
# Solved on 8th of September, 2025
import math


class Solution:
    def kthSmallestPath(self, destination: list[int], k: int) -> str:
        """
        Finds the k-th lexicographically smallest path from (0,0) to destination.
        :param destination: A list representing the [row, col] coordinates of the destination.
        :param k: The k-th smallest path to find.
        :return: A string representing the k-th lexicographically smallest path.
        """
        vMoves = destination[0]
        hMoves = destination[1]

        path = []

        totalMoves = vMoves + hMoves

        for _ in range(totalMoves):
            if hMoves > 0:
                pivot = math.comb((hMoves - 1 + vMoves), (hMoves - 1))

                if k <= pivot:
                    path.append('H')
                    hMoves -= 1
                else:
                    k -= pivot
                    path.append('V')
                    vMoves -= 1
            else:
                path.append('V')
                vMoves -= 1

        return "".join(path)