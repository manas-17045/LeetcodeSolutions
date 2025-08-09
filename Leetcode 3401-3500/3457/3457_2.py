# Leetcode 3457: Eat Pizzas!
# https://leetcode.com/problems/eat-pizzas/
# Solved on 9th of August, 2025
class Solution:
    def maxWeight(self, pizzas: list[int]) -> int:
        """
        Calculates the maximum total weight of pizzas that can be eaten over a period of days.
        :param pizzas: A list of integers representing the weights of the pizzas.
        :return: An integer representing the maximum total weight of pizzas.
        """
        n = len(pizzas)
        days = n // 4
        pizzas.sort()

        # Number of odd days
        odd = (days + 1) // 2
        # Number of even days
        even = days - odd

        # Sum the largest `odd` pizzas
        ans = sum(pizzas[-odd:]) if odd > 0 else 0

        # For the even days, pick every second pizza starting just before the odd-block
        i = n - odd - 2
        for _ in range(even):
            ans += pizzas[i]
            i -= 2

        return ans