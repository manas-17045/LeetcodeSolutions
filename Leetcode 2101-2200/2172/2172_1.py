# Leetcode 2172: Maximum AND Sum of Array
# https://leetcode.com/problems/maximum-and-sum-of-array/
# Solved on 10th of November, 2024

class Solution:
    def maximumANDSum(self, nums: list[int], numSlots: int) -> int:
        """
        Calculates the maximum possible AND sum by placing each number from `nums` into one of the `numSlots` slots.
        Each slot can hold at most two numbers. The AND sum is the sum of (number & slot_number) for all placed numbers.

        Args:
            nums: A list of integers to be placed in slots.
            numSlots: The number of available slots.

        Returns: The maximum possible AND sum.
        """
        def backtrack(index: int, slots: list[int], memo: dict) -> int:
            if index == len(nums):
                return 0

            state = (index, tuple(slots))
            if state in memo:
                return memo[state]

            max_sum = 0
            for slot in range(numSlots):
                if slots[slot] < 2:
                    slots[slot] += 1
                    curr_sum = (nums[index] & (slot + 1)) + backtrack(index + 1, slots, memo)
                    slots[slot] -= 1
                    max_sum = max(max_sum, curr_sum)

            memo[state] = max_sum
            return max_sum

        initial_slots = [0] * numSlots
        return backtrack(0, initial_slots, {})