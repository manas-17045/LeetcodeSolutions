# Leetcode 3257: Maximum Value Sum by Placing Three Rooks II
# https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/
# Solved on 3rd of November, 2025
import heapq


class Solution:
    def maximumValueSum(self, board: list[list[int]]) -> int:
        """
        Calculates the maximum value sum by placing three rooks on a chessboard
        such that no two rooks share the same row or column.

        Args:
            board: A 2D list of integers representing the chessboard, where board[r][c] is the value at (r, c).

        Returns:
            The maximum possible sum of values of three rooks placed according to the rules.
        """
        m = len(board)
        candidates = []

        for r in range(m):
            rowTop3 = heapq.nlargest(3, enumerate(board[r]), key=lambda x: x[1])
            for c, val in rowTop3:
                candidates.append((val, r, c))

        candidates.sort(key=lambda x: x[0], reverse=True)

        maxVal = -float('inf')
        numCandidates = len(candidates)

        for i in range(numCandidates):
            val1, r1, c1 = candidates[i]
            if val1 * 3 <= maxVal:
                break

            for j in range(i + 1, numCandidates):
                val2, r2, c2 = candidates[j]
                if val1 + val2 * 2 <= maxVal:
                    break
                if r2 == r1 or c2 == c1:
                    continue

                for k in range(j + 1, numCandidates):
                    val3, r3, c3 = candidates[k]
                    if val1 + val2 + val3 <= maxVal:
                        break
                    if r3 == r1 or r3 == r2 or c3 == c1 or c3 == c2:
                        continue

                    if val1 + val2 + val3 > maxVal:
                        maxVal = val1 + val2 + val3
                    break

        return maxVal