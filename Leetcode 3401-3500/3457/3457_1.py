# Leetcode 3457: Eat Pizzas!
# https://leetcode.com/problems/eat-pizzas/
# Solved on 9th of August, 2025
class Solution:
    def maxWeight(self, pizzas: list[int]) -> int:
        """
        Calculates the maximum total weight of pizzas that can be eaten.

        :param pizzas: A list of integers representing the weights of the pizzas.
        :return: An integer representing the maximum total weight of pizzas.
        """
        n = len(pizzas)
        m = n // 4
        k1 = (m + 1) // 2
        k2 = m // 2
        maxVal = max(pizzas)
        counts = [0] * (maxVal + 1)
        for w in pizzas:
            counts[w] += 1
        res = 0
        for val in range(maxVal, 0, -1):
            if k1 == 0:
                break
            if counts[val] == 0:
                continue
            t = counts[val] if counts[val] < k1 else k1
            res += val * t
            counts[val] -= t
            k1 -= t
        need = 2 * k2
        parity = 0
        for val in range(maxVal, 0, -1):
            if need == 0:
                break
            c = counts[val]
            if c == 0:
                continue
            t = c if c < need else need
            contrib = (t + parity) // 2
            res += val * contrib
            parity ^= (t & 1)
            need -= t
        return res