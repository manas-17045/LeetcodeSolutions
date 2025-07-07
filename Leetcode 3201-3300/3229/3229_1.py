# Leetcode 3229: Minimum Operations to Make Array Equal to Target
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/
# Solved on 7th of July, 2025
class Solution:
    def minimumOperatons(self, nums: list[int], target: list[int]) -> int:
        """
        Calculates the minimum number of operations to transform `nums` into `target`.

        An operation consists of choosing a subsegment of an array and incrementing
        or decrementing all elements in that subsegment by 1.

        Args:
            nums: The initial list of integers.
            target: The target list of integers.

        Returns:
            The minimum total number of operations required.
        """
        n = len(nums)

        incrementOps = 0
        decrementOps = 0

        lastPosDiff = 0
        lastNegDiff = 0

        for i in range(n):
            currentDiff = target[i] - nums[i]

            currentPosDiff = max(0, currentDiff)
            if currentPosDiff > lastPosDiff:
                incrementOps += currentPosDiff - lastPosDiff

            currentNegDiff = min(0, -currentDiff)
            if currentNegDiff > lastNegDiff:
                decrementOps += currentNegDiff - lastNegDiff

            lastPosDiff = currentPosDiff
            lastNegDiff = currentNegDiff

        return incrementOps + decrementOps