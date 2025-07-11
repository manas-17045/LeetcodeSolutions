# Leetcode 1944: Number of Visible People in a Queue
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/
# Solved on 11th of July, 2025
class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        """
        Calculates the number of people each person can see to their right.

        Args:
            heights (list[int]): A list of integers representing the heights of people.

        Returns:
            list[int]: A list where ans[i] is the number of people the i-th person can see.
        """
        n = len(heights)
        ans = [0] * n
        stack: list[int] = []   # will store heights in decreasing order

        # Scan from rightmost person to leftmost
        for i in range((n - 1), -1, -1):
            h = heights[i]
            # Pop all shorter people: they're visible to you
            while stack and stack[-1] < h:
                stack.pop()
                ans[i] += 1

            # If there's still someone on the stack, they're taller and visible
            if stack:
                ans[i] += 1

            # Put yourself on the stack
            stack.append(h)

        return ans