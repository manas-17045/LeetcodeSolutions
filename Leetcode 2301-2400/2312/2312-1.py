# Leetcode 2312: Selling Pieces of Wood
# https://leetcode.com/problems/selling-pieces-of-wood/
# Solved on 10th of September, 2025
class Solution:
    def sellingWood(self, m: int, n: int, prices: list[list[int]]) -> int:
        """
        Calculates the maximum profit obtainable by selling pieces of wood.

        Args:
            m (int): The height of the original piece of wood.
            n (int): The width of the original piece of wood.
            prices (list[list[int]]): A list of available prices, where each inner list `[h, w, price]` represents the price for a piece of wood of size `h x w`.

        Returns:
            int: The maximum profit that can be obtained from selling pieces of wood.
        """

        maxProfitForSize = [[0] * (n + 1) for _ in range(m + 1)]

        for h, w, price in prices:
            maxProfitForSize[h][w] = price

        for height in range(1, m + 1):
            for width in range(1, n + 1):
                # Horizontal cuts
                for cutHeight in range(1, height // 2 + 1):
                    profitFromCut = maxProfitForSize[cutHeight][width] + maxProfitForSize[height - cutHeight][width]
                    maxProfitForSize[height][width] = max(maxProfitForSize[height][width], profitFromCut)

                # Vertical cuts
                for cutWidth in range(1, width // 2 + 1):
                    profitFromCut = maxProfitForSize[height][cutWidth] + maxProfitForSize[height][width - cutWidth]
                    maxProfitForSize[height][width] = max(maxProfitForSize[height][width], profitFromCut)

        return maxProfitForSize[m][n]