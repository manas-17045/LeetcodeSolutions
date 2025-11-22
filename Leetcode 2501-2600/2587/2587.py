# Leetcode 2587: Rearrange Array to Maximize Prefix Score
# https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/
# Solved on 22nd of November, 2025
class Solution:
    def maxScore(self, nums: list[int]) -> int:
        """
        Rearranges the array nums to maximize the number of positive prefix sums.

        Args:
            nums: A list of integers.
        Returns:
            The maximum number of positive prefix sums achievable.
        """
        nums.sort(reverse=True)
        currentPrefixSum = 0
        score = 0
        for num in nums:
            currentPrefixSum += num
            if currentPrefixSum > 0:
                score += 1
            else:
                break
        return score