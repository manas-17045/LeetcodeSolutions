# Leetcode 3181: Maximum Total Reward Using Operations II
# https://leetcode.com/problems/maximum-total-reward-using-operations-ii/
# Solved on 28th of February, 2026
class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        """
        Calculates the maximum total reward possible using bitset optimization.

        :param rewardValues: A list of integers representing available rewards.
        :return: The maximum total reward achievable.
        """
        uniqueRewards = sorted(set(rewardValues))
        reachableSums = 1

        for reward in uniqueRewards:
            validMask = (1 << reward) - 1
            reachableSums |= (reachableSums & validMask) << reward

        return reachableSums.bit_length() - 1