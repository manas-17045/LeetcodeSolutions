# Leetcode 2312: Selling Pieces of Wood
# https://leetcode.com/problems/selling-pieces-of-wood/
# Solved on 10th of September, 2025
class Solution:
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        """
        Calculates the maximum profit obtainable by selling pieces of wood cut from an m x n board.
        Args:
            m (int): The height of the original wood board.
            n (int): The width of the original wood board.
            prices (list[list[int]]): A list of lists, where each inner list [h, w, p] represents
                                      a piece of wood of height h and width w that can be sold for price p.
        Returns:
            int: The maximum profit that can be obtained.
        """
        # Map exact shapes to given prices (no rotation allowed)
        price_map = {(h, w): p for h, w, p in prices}

        # dp array: (m+1) x (n+1), 0-initialized
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill DP from small to large sizes
        for h in range(1, m + 1):
            for w in range(1, n + 1):
                # If there's a direct price for this exact shape, use it
                if (h, w) in price_map:
                    dp[h][w] = price_map[(h, w)]

                # Try horizontal cuts: split into k x w and (h-k) x w
                # Only iterate k up to h//2 and use symmetry to reduce checks
                for k in range(1, h // 2 + 1):
                    val = dp[k][w] + dp[h - k][w]
                    if val > dp[h][w]:
                        dp[h][w] = val

                # Try vertical cuts: split into h x k and h x (w-k)
                for k in range(1, w // 2 + 1):
                    val = dp[h][k] + dp[h][w - k]
                    if val > dp[h][w]:
                        dp[h][w] = val

        return dp[m][n]