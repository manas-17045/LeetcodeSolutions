# Leetcode 2289: Steps to Make Array Non-decreasing
# https://leetcode.com/problems/steps-to-make-array-non-decreasing/
# Solved on 7th of September, 2025
class Solution:
    def totalSteps(self, nums: list[int]) -> int:
        """
        Calculates the maximum number of steps required to remove all elements from the array.
        An element `nums[i]` is removed if `nums[i] > nums[i+1]` in a single step.

        Args:
            nums (list[int]): The input array of integers.
        Returns:
            int: The maximum number of steps required.
        """
        stack = []  # pairs (value, steps_to_remove)
        ans = 0

        for x in nums:
            cur_steps = 0
            # Pop smaller or equal values; they can't block x from being removed
            while stack and x >= stack[-1][0]:
                cur_steps = max(cur_steps, stack[-1][1])
                stack.pop()

            if not stack:
                # Nothing to the left that is greater, x will never be removed
                cur_steps = 0
            else:
                # There is a greater value on the left that survives,
                # so x will be removed one round after the max of popped times
                cur_steps += 1

            ans = max(ans, cur_steps)
            stack.append((x, cur_steps))

        return ans