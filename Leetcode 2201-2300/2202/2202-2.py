# Leetcode 2202: Maximize the Topmost Element After K Moves
# https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/
# Solved on 1st of September, 2025
class Solution:
    def maximumTop(self, nums: list[int], k: int) -> int:
        """
        :param nums: A list of integers representing the stack.
        :param k: An integer representing the number of operations.
        :return: The maximum possible value of the top element after exactly k operations.
        """
        n = len(nums)

        if k == 0:
            return nums[0]

        if n == 1:
            return -1 if (k % 2 == 1) else nums[0]

        if k > n:
            return max(nums)

        best_from_prefix = float('inf')
        if k - 1 > 0:
            best_from_prefix = max(nums[:(k - 1)])

        candidate_from_index_k = nums[k] if k < n else float('inf')
        return max(best_from_prefix, candidate_from_index_k)