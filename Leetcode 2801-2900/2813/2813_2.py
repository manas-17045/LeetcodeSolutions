# Leetcode 2813: Maximum Elegance of a K-Length Subsequence
# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/
# Solved on 11th of July, 2025
import heapq
from collections import defaultdict


class Solution:
    def findMaximumElegance(self, items: list[list[int]], k: int) -> int:
        """
        Calculates the maximum elegance achievable by selecting k items.

        Elegance is defined as total_profit + distinct_categories^2.
        The strategy involves:
        1. Sorting items by profit in descending order.
        2. Picking the top k items initially to form a base set.
        3. Identifying duplicate categories within the base set and storing their profits in a min-heap.
        4. Identifying potential new categories from the remaining items (those not in the initial k items
           and not already present in the base set's categories).
        5. Greedily swapping out the lowest-profit item from a duplicate category in the base set
           with the highest-profit item from a new category, as long as it increases elegance.

        Args:
            items: A list of lists, where each inner list `[profit, category]` represents an item.
            k: The number of items to select.

        Returns:
            The maximum elegance achievable.
        """
        items.sort(key=lambda x: -x[0])

        total_profit = 0
        cat_count = defaultdict(int)
        duplicate_profits = []  # min-heap of profits from duplicate-category picks

        # Build initial window of size k
        for i in range(k):
            profit, cat = items[i]
            total_profit += profit
            cat_count[cat] += 1
            if cat_count[cat] > 1:
                # This pick is a duplicate category => record its profit for potential swap
                heapq.heappush(duplicate_profits, profit)

        distinct = len(cat_count)
        # Initial elegance
        best = total_profit + distinct * distinct

        # Collect potential new-category items from the rest, in profit order
        seen = set(cat_count.keys())
        new_cat_profits = []
        for profit, cat in items[k:]:
            if cat not in seen:
                seen.add(cat)
                new_cat_profits.append(profit)

        # We want to swap in the highest-profit new categories first
        new_cat_profits.sort(reverse=True)

        # Greedy swaps: each swap  raises distinct by 1, removes smallest duplicate profit, adds this new profit
        for new_profit in new_cat_profits:
            if not duplicate_profits:
                break
            # Lose the smallest-profit duplicate, gain this new category profit
            dup_profit = heapq.heappop(duplicate_profits)
            total_profit += new_profit - dup_profit
            distinct += 1
            best = max(best, (total_profit + distinct * distinct))

        return best