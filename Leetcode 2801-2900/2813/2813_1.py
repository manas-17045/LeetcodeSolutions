# Leetcode 2813: Maximum Elegance of a K-Length Subsequence
# https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/
# Solved on 11th of July, 2025
class Solution:
    def findMaximumElegance(self, items: list[list[int]], k: int) -> int:
        """
        Calculates the maximum elegance of a k-length subsequence.

        The elegance of a subsequence is defined as `total_profit + total_distinct_categories^2`.
        The goal is to select `k` items such that this elegance is maximized.

        Args:
            items: A list of lists, where each inner list `[profit, category]` represents an item.
            k: The desired length of the subsequence.
        """
        items.sort(key=lambda item: item[0], reverse=True)

        totalProfit = 0
        seenCategories = set()
        duplicates = []

        for i in range(k):
            profit, category = items[i]
            totalProfit += profit
            if category in seenCategories:
                duplicates.append(i)
            else:
                seenCategories.add(category)

        maxElegance = totalProfit + len(seenCategories)**2

        for i in range(k, len(items)):
            if not duplicates:
                break

            profit, category = items[i]

            if category not in seenCategories:
                removedProfit = duplicates.pop()

                totalProfit = totalProfit - removedProfit + profit
                seenCategories.add(category)

                currentElegance = totalProfit + len(seenCategories)**2
                if currentElegance > maxElegance:
                    maxElegance = currentElegance

        return maxElegance