# Leetcode 2931: Maximum Spending After Buying Items
# https://leetcode.com/problems/maximum-spending-after-buying-items/
# Solved on 2nd of July, 2025
import heapq


class Solution:
    def maxSpending(self, values: list[list[int]]) -> int:
        """
        Calculates the maximum spending possible by buying items from different shops.

        The strategy is to always buy the cheapest available item on the current day,
        as this maximizes the spending due to the increasing multiplier (day number).
        A min-heap is used to efficiently retrieve the cheapest item across all shops.

        Args:
            values: A list of lists of integers, where values[i][j] represents the
                    price of the j-th item in the i-th shop. Items in each shop
                    are sorted in ascending order of price.

        Returns:
            The maximum total spending.
        """
        numShops = len(values)
        numItems = len(values[0])

        minHeap = []
        for i in range(numShops):
            itemValue = values[i][numItems - 1]
            shopIndex = i
            itemIndex = numItems - 1
            heapq.heappush(minHeap, (itemValue, shopIndex, itemIndex))

        totalSpending = 0
        day = 1

        while minHeap:
            itemValue, shopIndex, itemIndex = heapq.heappop(minHeap)

            totalSpending += itemValue * day
            day += 1

            if itemIndex > 0:
                nextItemIndex = itemIndex - 1
                nextItemValue = values[shopIndex][nextItemIndex]
                heapq.heappush(minHeap, (nextItemValue, shopIndex, nextItemIndex))

        return totalSpending