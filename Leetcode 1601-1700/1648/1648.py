# Leetcode 1648: Sell Diminishing-Valued Colored Balls
# https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
# Solved on 1st of December, 2025
class Solution:
    def maxProfit(self, inventory: list[int], orders: int) -> int:
        """
        Calculates the maximum profit that can be obtained from selling colored balls.

        Args:
            inventory (list[int]): A list of integers representing the number of balls of each color.
            orders (int): The total number of balls to sell.

        Returns:
            int: The maximum profit modulo 10^9 + 7.
        """
        inventory.sort(reverse=True)
        inventory.append(0)
        profit = 0
        width = 0
        mod = 10 ** 9 + 7

        for i in range(len(inventory) - 1):
            width += 1
            currentVal = inventory[i]
            nextVal = inventory[i + 1]

            if currentVal == nextVal:
                continue

            count = width * (currentVal - nextVal)

            if orders >= count:
                profit += width * (currentVal + nextVal + 1) * (currentVal - nextVal) // 2
                orders -= count
            else:
                fullRows = orders // width
                remainder = orders % width
                lastVal = currentVal - fullRows
                profit += width * (currentVal + lastVal + 1) * fullRows // 2
                profit += remainder * lastVal
                break

        return profit % mod