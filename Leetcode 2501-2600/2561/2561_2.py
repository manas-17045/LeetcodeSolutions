# Leetcode 2561: Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits/
# Solved on 10th of June, 2025
from collections import Counter


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        """
        Calculates the minimum cost to make the two baskets contain the same
        number of each fruit type.

        The cost of swapping two fruits is the minimum of their values.
        A two-step swap (swapping a fruit from basket1 with the global minimum,
        then swapping the global minimum with a fruit from basket2) is also
        possible and might be cheaper.

        Args:
            basket1: A list of integers representing the fruits in the first basket.
            basket2: A list of integers representing the fruits in the second basket.

        Returns:
            The minimum cost to make the baskets have the same fruit counts,
            or -1 if it's impossible.
        """
        # Count frequencies in each basket
        c1 = Counter(basket1)
        c2 = Counter(basket2)

        # Global minimum fruit cost (for possible two-step swaps)
        global_min = min(min(basket1), min(basket2))

        # Check that every fruit value has even total frequency
        all_keys = set(c1) | set(c2)
        for v in all_keys:
            if (c1[v] + c2[v]) % 2:
                return -1

        # Gather the "extra" fruits that need to move out of each basket.
        extras1 = []
        extras2 = []

        for v in all_keys:
            diff = c1[v] - c2[v]
            if diff > 0:
                extras1.extend([v] * (diff // 2))
            elif diff < 0:
                extras2.extend([v] * ((-diff) // 2))

        # They must be the same length
        n = len(extras1)
        if n == 0:
            return 0

        # Sort extras so we can pair smallest from one side with largest from the other side
        extras1.sort()
        extras2.sort(reverse=True)

        cost = 0
        two_step = 2 * global_min
        for x, y in zip(extras1, extras2):
            cost += min(x, y, two_step)

        return cost