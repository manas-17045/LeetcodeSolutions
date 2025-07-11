# Leetcode 1944: Number of Visible People in a Queue
# https://leetcode.com/problems/number-of-visible-people-in-a-queue/
# Solved on 11th of July, 2025
class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        """
        Calculates the number of people each person in a queue can see to their right.

        Args:
            heights (list[int]): A list of integers representing the heights of people in the queue.
        Returns:
            list[int]: A list of integers where answer[i] is the number of people the i-th person can see.
        """
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range((n - 1), -1, -1):
            currentHeight = heights[i]
            visibleCount = 0

            while stack and stack[-1] < currentHeight:
                stack.pop()
                visibleCount += 1

            if stack:
                visibleCount += 1

            stack.append(currentHeight)
            answer[i] = visibleCount

        return answer