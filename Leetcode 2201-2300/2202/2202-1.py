# Leetcode 2202: Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
# Solved on 1st of September, 2025
class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        """
        Maximizes the topmost element of a pile after exactly k moves.

        Args:
            nums: A list of integers representing the pile.
            k: The exact number of moves to perform.

        Returns: The maximum possible topmost element.
        """

        numElements = len(nums)

        if numElements == 1 and k % 2 == 1:
            return -1

        if k > numElements:
            return max(nums)

        if k == numElements:
            return max(nums[:(k - 1)]) if k > 0 else -1

        maxVal = nums[k]

        if k > 0:
            prefixMax = max(nums[:(k - 1)]) if k > 1 else -1
            maxVal = max(maxVal, prefixMax)

        return maxVal