# Leetcode 3939: Count Non Adjacent Subsets in a Rooted Tree
# https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/
# Solved on 7th of June, 2026
class Solution:
    def countValidSubsets(self, parent: list[int], nums: list[int], k: int) -> int:
        """
        Calculates the number of non-adjacent subsets in a rooted tree where the sum of elements modulo k is 0.

        :param parent: A list of integers where parent[i] is the parent of node i. parent[0] is -1.
        :param nums: A list of integers representing the value of each node.
        :param k: The divisor for the subset sum condition.
        :return: The count of valid subsets modulo 10^9 + 7.
        """
        n = len(parent)
        modVal = 10**9 + 7
        dp0 = [[0] * k for _ in range(n)]
        dp1 = [[0] * k for _ in range(n)]

        for i in range(n):
            dp0[i][0] = 1
            dp1[i][nums[i] % k] = 1

        for u in range(n - 1, 0, -1):
            p = parent[u]
            newDp0 = [0] * k
            newDp1 = [0] * k

            activeDp0P = [(r, val) for r, val in enumerate(dp0[p]) if val]
            activeDp1P = [(r, val) for r, val in enumerate(dp1[p]) if val]

            activeVSum = []
            for r in range(k):
                sm = dp0[u][r] + dp1[u][r]
                if sm >= modVal:
                    sm -= modVal
                if sm > 0:
                    activeVSum.append((r, sm))

            activeDp0U = [(r, val) for r, val in enumerate(dp0[u]) if val]

            for r1, val1 in activeDp0P:
                for r2, val2 in activeVSum:
                    nxt = r1 + r2
                    if nxt >= k:
                        nxt -= k
                    newDp1[nxt] += val1 * val2

            for r in range(k):
                dp0[p][r] = newDp0[r] % modVal
                dp1[p][r] = newDp1[r] % modVal

        return (dp0[0][0] + dp1[0][0] - 1) % modVal