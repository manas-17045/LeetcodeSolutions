# Leetcode 2931: Maximum Spending After Buying Items
# https://leetcode.com/problems/maximum-spending-after-buying-items/
# Solved on 2nd of July, 2025
import heapq


class Solution:
    def maxSpending(self, values: list[list[int]]) -> int:
        """
        Calculates the maximum total spending by strategically buying items from multiple shops.

        You are given a 2D integer array `values`, where `values[i][j]` represents the value
        of the j-th item in the i-th shop. Each shop has `n` items.

        You must buy all `m * n` items, one item per day. On day `d` (1-indexed), the value
        of an item you buy is multiplied by `d`. You want to maximize your total spending.

        The strategy is to always buy the item with the smallest *current* value among all
        available items across all shops. This is because smaller values benefit less from
        being multiplied by larger day numbers.

        Args:
            values: A list of lists of integers, where `values[i][j]` is the value of the j-th item in shop i.

        Returns:
            The maximum total spending.
        """
        m = len(values)
        if m == 0:
            return 0
        # Number of items per shop (assumes all shops have same length n)
        n = len(values[0])
        # pointers[i] = index of the rightmost remaining item in shop i
        ptr = [n - 1] * m

        # Build a heap of (base_value, shop_index) for each shop's current rightmost item
        heap = []
        for i in range(m):
            if ptr[i] >= 0:
                heap.append((values[i][ptr[i]], i))
        heapq.heapify(heap)

        total = 0
        # We have to buy all m * n items, one per day
        days = m * n
        for day in range(1, days + 1):
            base_val, shop = heapq.heappop(heap)
            total += base_val * day
            # Advance in that shop
            ptr[shop] -= 1
            if ptr[shop] >= 0:
                # Push the next (still the smallest remaining) item
                heapq.heappush(heap, (values[shop][ptr[shop]], shop))

        return total