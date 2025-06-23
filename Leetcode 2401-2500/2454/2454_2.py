# Leetcode 2454: Next Greater Element IV
# https://leetcode.com/problems/next-greater-element-iv/
# Solved on 23rd of June, 2025
class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        """
        Given a 0-indexed array nums of non-negative integers, find the second greater element for every element in nums.

        The second greater element of nums[i] is nums[j] such that:
        1. j > i
        2. nums[j] > nums[i]
        3. There exists exactly one index k such that i < k < j and nums[k] > nums[i].

        If there is no such nums[j], the second greater element is -1.

        Return an integer array answer, where answer[i] is the second greater element of nums[i].
        """
        n = len(nums)
        # Answer array, default -1
        answer = [-1] * n

        stk1, stk2 = [], []

        for i, x in enumerate(nums):
            # Resolve seconds, any index on stk2 whose second greater is x
            while stk2 and nums[stk2[-1]] < x:
                answer[stk2.pop()] = x

            # Promote from first-waiting to second-waiting whenever x is their first greater
            temp = []
            while stk1 and nums[stk1[-1]] < x:
                temp.append(stk1.pop())

            while temp:
                stk2.append(temp.pop())

            stk1.append(i)

        return answer