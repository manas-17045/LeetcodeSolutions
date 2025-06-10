# Leetcode 2561: Rearranging Fruits
# https://leetcode.com/problems/rearranging-fruits/
# Solved on 10th of June, 2025
from collections import Counter


class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        """
        Calculates the minimum cost to rearrange fruits such that both baskets have an equal number of each fruit.

        Args:
            basket1: A list of integers representing the fruits in the first basket.
            basket2: A list of integers representing the fruits in the second basket.

        Returns:
            The minimum cost to rearrange the fruits. Returns -1 if it's impossible to achieve the target configuration.

        The algorithm works by first counting the total occurrences of each fruit. If any fruit has an odd total count,
        it's impossible to distribute them equally, so we return -1. Otherwise, we identify the excess fruits in each
        basket compared to the target equal distribution. We then calculate the minimum cost to swap these excess fruits,
        considering both direct swaps and indirect swaps through the minimum-cost fruit.
        """
        counts = Counter(basket1)
        counts.update(basket2)

        minFruit = float('inf')

        for fruit, count in counts.items():
            if count % 2 != 0:
                return -1
            minFruit = min(minFruit, fruit)

        countInBasket1 = Counter(basket1)

        excessInB1 = []
        excessInB2 = []

        for fruit, totalCount in counts.items():
            targetCount = totalCount // 2
            currentCountInB1 = countInBasket1.get(fruit, 0)
            diff = currentCountInB1 - targetCount

            if diff > 0:
                excessInB1.extend([fruit] * diff)
            else:
                excessInB2.extend([fruit] * -diff)

        excessInB1.sort()
        excessInB2.sort(reverse=True)

        totalCost = 0
        for i in range(len(excessInB1)):
            fruitFromB1 = excessInB1[i]
            fruitFromB2 = excessInB2[i]

            directSwapCost = min(fruitFromB1, fruitFromB2)
            indirectSwapCost = 2 * minFruit

            totalCost += min(directSwapCost, indirectSwapCost)

        return totalCost