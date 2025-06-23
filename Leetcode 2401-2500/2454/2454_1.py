# Leetcode 2454: Next Greater Element IV
# https://leetcode.com/problems/next-greater-element-iv/
# Solved on 2nd of November, 2024
class Solution:
    def secondGreaterElement(self, nums: list[int]) -> list[int]:
        """
        Finds the second greater element for each element in the input array.

        For each element nums[i], the second greater element is the smallest element
        nums[j] such that j > i, nums[j] > nums[i], and there exists at least one
        element nums[k] such that i < k < j and nums[k] > nums[i].
        If no such element exists, the answer for nums[i] is -1.

        Args:
            nums: A list of integers.
        Returns:
            A list of integers representing the second greater element for each element.
        """
        n = len(nums)
        answer = [-1] * n
        stack1 = []
        stack2 = []

        for i in range(n):
            while stack2 and nums[stack2[-1]] < nums[i]:
                answer[stack2.pop()] = nums[i]

            temp = []
            while stack1 and nums[stack1[-1]] < nums[i]:
                temp.append(stack1.pop())

            while temp:
                stack2.append(temp.pop())

            stack1.append(i)

        return answer