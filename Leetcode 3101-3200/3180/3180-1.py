# Leetcode 3180: Maximum Total Reward Using Operations I
# https://leetcode.com/problems/maximum-total-reward-using-operations-i/
# Solved on 20th of September, 2025
class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        """
        Calculates the maximum total reward achievable by selecting a subset of reward values.
        A reward value `r` can only be chosen if the current total reward `x` is less than `r`.

        Args:
            rewardValues: A list of integers representing the available reward values.

        Returns:
            The maximum total reward that can be achieved.
        """
        rewardValues.sort()
        possibleRewards = {0}

        for reward in rewardValues:
            newRewards = set()
            for currentReward in possibleRewards:
                if currentReward < reward:
                    newRewards.add(currentReward + reward)
            possibleRewards.update(newRewards)

        return max(possibleRewards)