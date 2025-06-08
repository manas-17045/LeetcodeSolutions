# Leetcode 1402: Reducing Dishes
# https://leetcode.com/problems/reducing-dishes/
# Solved on 8th of June, 2025

class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        """
        Calculates the maximum total like-time coefficient.

        The like-time coefficient of a dish is the product of its satisfaction
        level and the time it's cooked. The total like-time coefficient is the
        sum of the like-time coefficients of all dishes cooked. We can choose
        to cook any subset of dishes, and the time taken to cook each dish is
        1 unit. The dishes are cooked in some order, and the time assigned to
        each dish is its position in the cooking order (starting from 1).

        Args:
            satisfaction: A list of integers representing the satisfaction levels of dishes.

        Returns:
            The maximum total like-time coefficient.
        """
        # Sort the array so that we can consider the largest satisfaction first
        satisfaction.sort()

        total, prefix_sum = 0, 0
        # Greedily include dishes from highest satisfaction downwards
        for s in reversed(satisfaction):
            # If adding this dish increases the cumulative satisfaction prefix_sum,
            # then it's worth including it (and all previously chosen dishes get
            # shifted one time unit later, adding prefix_sum + s to the answer).
            if prefix_sum + s > 0:
                prefix_sum += s
                total += prefix_sum
            else:
                # Further (smaller) values will only make prefix_sum smaller
                break

        return total