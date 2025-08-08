# Leetcode 1467: Probability of a Two Boxes Having The Same Number of Distinct Balls
# https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/
# Solved on 8th of August, 2025
import math
from collections import defaultdict


class Solution:
    def getProbability(self, balls: list[int]) -> float:
        """
        Calculates the probability that two boxes have the same number of distinct colors and the same total number of balls.

        :param balls: A list of integers where balls[i] represents the number of balls of color i.
        :return: The probability as a float.
        """
        total = sum(balls)
        half = total // 2

        # Precompute combination values for each color
        combs = [[math.comb(b, k) for k in range(b + 1) for b in balls]]

        dp = {(0, 0): 1}

        for i, b in enumerate(balls):
            newDp = defaultdict(int)
            for (assigned, diff), ways in dp.items():
                # Try all splits k balls into box 1
                for k in range(b + 1):
                    new_assigned = assigned + k
                    if new_assigned > half:
                        continue
                    # Update diff
                    if k == 0:
                        new_diff = diff - 1
                    elif k == b:
                        new_diff = diff + 1
                    else:
                        new_diff = diff
                    newDp[(new_assigned, new_diff)] += ways * combs[i][k]

            dp = newDp

        numerator = dp.get((half, 0), 0)
        denominator = math.comb(total, half)

        return numerator / denominator