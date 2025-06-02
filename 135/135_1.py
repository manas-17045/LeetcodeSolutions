# Leetcode 135: Candy
# https://leetcode.com/problems/candy/
# Solved on 2nd of June, 2025

class Solution:
    def candy(self, ratings: list[int]) -> int:
        """
        Distributes candies to children based on their ratings.

        Each child must have at least one candy.
        Children with a higher rating get more candies than their neighbors.

        Args:
            ratings: A list of integers representing the ratings of the children.

        Returns:
            The minimum number of candies required to distribute.
        """

        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        totalCandies = sum(candies)
        return totalCandies