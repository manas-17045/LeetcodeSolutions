# Leetcode 3418: Maximum Amount of Money Robot Can Earn
# https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/
# Solved on 16th of August, 2025
class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        """
        Calculates the maximum amount of coins that can be collected.
        :param coins: A 2D list of integers representing the coins in each cell.
        :return: The maximum amount of coins that can be collected.
        """
        if not coins or not coins[0]:
            return 0

        m = len(coins)
        n = len(coins[0])
        NEG_INF = -10**18

        prev = [[NEG_INF] * 3 for _ in range(n)]

        for i in range(m):
            cur = [[NEG_INF] * 3 for _ in range(n)]
            for j in range(n):
                v = coins[i][j]

                if i == 0 and j == 0:
                    if v >= 0:
                        cur[0][0] = v
                    else:
                        cur[0][0] = v
                        cur[0][1] = 0
                    continue

                for k in range(3):
                    from_top = prev[j][k] if i > 0 else NEG_INF
                    from_left = cur[j - 1][k] if j > 0 else NEG_INF
                    best_prev_no_use = from_top if from_top > from_left else from_left

                    if v >= 0:
                        if best_prev_no_use != NEG_INF:
                            cur[j][k] = max(cur[j][k], best_prev_no_use + v)
                    else:
                        if best_prev_no_use != NEG_INF:
                            cur[j][k] = max(cur[j][k], best_prev_no_use + v)
                        if k >= 1:
                            from_top_prev_used = prev[j][k - 1] if i > 0 else NEG_INF
                            from_left_prev_used = cur[j - 1][k - 1] if j > 0 else NEG_INF
                            best_prev_used = from_top_prev_used if from_top_prev_used > from_left_prev_used else from_left_prev_used
                            if best_prev_used != NEG_INF:
                                cur[j][k] = max(cur[j][k], best_prev_used)

            prev = cur

        return max(prev[n - 1])