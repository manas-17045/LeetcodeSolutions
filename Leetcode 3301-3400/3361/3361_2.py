# Leetcode 3361: Shift Distance Between Two Strings
# https://leetcode.com/problems/shift-distance-between-two-strings/
# Solved on 4th of July, 2025
class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: list[int], previousCost: list[int]) -> int:
        """
        Calculates the minimum total cost to transform string `s` into string `t`.

        Each character in `s` can be transformed into a character in `t` by
        shifting it cyclically. The cost of shifting 'a' to 'b' is `nextCost[0]`,
        'b' to 'c' is `nextCost[1]`, and so on. Similarly, the cost of shifting
        'b' to 'a' is `previousCost[1]`, 'c' to 'b' is `previousCost[2]`, etc.

        Args:
            s: The source string.
            t: The target string.
            nextCost: A list of integers where `nextCost[i]` is the cost to shift
                      the i-th letter of the alphabet to the (i+1)-th letter.
            previousCost: A list of integers where `previousCost[i]` is the cost to shift
                          the i-th letter of the alphabet to the (i-1)-th letter.

        Returns:
            The minimum total cost to transform `s` into `t`.
        """
        A = 26

        INF = 10**30
        dist = [[INF] * A for _ in range(A)]
        for i in range(A):
            dist[i][i] = 0

        for i in range(A):
            dist[i][(i + 1) % A] = min(dist[i][(i + 1) % A], nextCost[i])
            dist[i][(i - 1) % A] = min(dist[i][(i - 1) % A], previousCost[i])

        # Floyd-Warshall over 26 nodes
        for k in range(A):
            dk = dist[k]
            for i in range(A):
                di = dist[i]
                via = di[k]
                if via == INF:
                    continue
                for j in range(A):
                    nd = via + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        # Sum up per-position conversion cost
        total = 0
        for cs, ct in zip(s, t):
            i = ord(cs) - ord('a')
            j = ord(ct) - ord('a')
            total += dist[i][j]

        return total