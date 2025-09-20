# Leetcode 3180: Maximum Total Reward Using Operations I
# https://leetcode.com/problems/maximum-total-reward-using-operations-i/
# Solved on 20th of September, 2025
class Solution:
    def maxTotalRewards(self, rewardValues: list[int]) -> int:
        """
        Calculates the maximum total rewards that can be collected.
        :param rewardValues: A list of integers representing the values of rewards.
        :return: An integer representing the maximum total rewards.
        """
        # Sort rewardValues in ascending
        a = sorted(rewardValues)
        total = sum(a)

        possible = bytearray(total + 1)
        possible[0] = 1
        max_sum = 0

        for v in a:
            upper = min(v, (max_sum + 1))
            for s in range(upper):
                if possible[s]:
                    new_s = s + v
                    if not possible[new_s]:
                        possible[new_s] = 1
                        if new_s > max_sum:
                            max_sum = new_s

        return max_sum