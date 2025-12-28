# Leetcode 3679: Minimum Discards to Balance Inventory
# https://leetcode.com/problems/minimum-discards-to-balance-inventory/
# Solved on 28th of December, 2025
class Solution:
    def minArrivalsToDiscard(self, arrivals: list[int], w: int, m: int) -> int:
        """
        Calculates the minimum number of items to discard to balance the inventory.
        :param arrivals: A list of integers representing the arrival of items.
        :param w: An integer representing the window size.
        :param m: An integer representing the maximum count for any single item type.
        :return: An integer representing the minimum number of discards.
        """
        n = len(arrivals)
        keptStatus = [False] * n
        itemCounts = [0] * 100005
        discardCount = 0

        for i in range(n):
            if i >= w:
                removeIndex = i - w
                if keptStatus[removeIndex]:
                    removeValue = arrivals[removeIndex]
                    itemCounts[removeValue] -= 1

            currentValue = arrivals[i]
            if itemCounts[currentValue] < m:
                keptStatus[i] = True
                itemCounts[currentValue] += 1
            else:
                discardCount += 1

        return discardCount