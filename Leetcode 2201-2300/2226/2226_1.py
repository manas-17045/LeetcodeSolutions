# Leetcode 2226: Maximum Candies Allocated to K Children
# https://leetcode.com/problems/maximum-candies-allocated-to-k-children/
# Solved on 3rd of August, 2025
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        """
        Calculates the maximum number of candies that can be allocated to each of k children,
        given a list of candy piles. Each pile can be divided into any number of pieces.

        Args:
            candies (list[int]): A list of integers representing the number of candies in each pile.
            k (int): The number of children to distribute candies to.

        Returns:
            int: The maximum number of candies each child can receive.
        """
        totalCandies = sum(candies)
        if totalCandies < k:
            return 0

        left = 1
        right = totalCandies // k
        maxCandies = 0

        while left <= right:
            candiesPerChild = left + (right - left) // 2
            
            if candiesPerChild == 0:
                left = candiesPerChild + 1
                continue

            childrenSatisfied = 0
            for pile in candies:
                childrenSatisfied += pile // candiesPerChild

            if childrenSatisfied >= k:
                maxCandies = candiesPerChild
                left = candiesPerChild + 1
            else:
                right = candiesPerChild - 1

        return maxCandies