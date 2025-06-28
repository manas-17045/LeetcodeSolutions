# Leetcode 2708: Maximum Strength of a Group
# https://leetcode.com/problems/maximum-strength-of-a-group/
# Solved on 28th of June, 2025
class Solution:
    def maxStrength(self, nums: list[int]) -> int:
        """
        Calculates the maximum strength of a group, which is the maximum product
        of a non-empty subsequence of `nums`.

        Args:
            nums: A list of integers.
        Returns:
            The maximum strength of a group.
        """
        if len(nums) == 1:
            return nums[0]

        positives = []
        negatives = []
        hasZero = False

        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                hasZero = True

        if not positives and len(negatives) <= 1:
            if hasZero:
                return 0
            if len(negatives) == 1:
                return negatives[0]
            return 0

        maxStrength = 1
        for p in positives:
            maxStrength *= p

        negatives.sort()

        if len(negatives) % 2 == 1:
            negativesToInclude = negatives[:-1]
        else:
            negativesToInclude = negatives

        for n in negativesToInclude:
            maxStrength *= n

        return maxStrength