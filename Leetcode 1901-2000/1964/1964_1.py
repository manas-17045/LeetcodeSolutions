# Leetcode 1964: Find the Longest Valid Obstacle Course at Each Position
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# Solved on 22nd of July, 2025
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        """
        Finds the length of the longest valid obstacle course at each position.
        :param obstacles: A list of integers representing the heights of obstacles.
        :return: A list of integers, where each element results[i] is the length
                 of the longest valid obstacle course ending at index i.
        """
        tails = []
        results = []
        for obstacle in obstacles:
            # Find the insertion point for the current obstacle in the tails list.
            insertionPoint = bisect.bisect_right(tails, obstacle)

            if insertionPoint == len(tails):
                tails.append(obstacle)
            else:
                tails[insertionPoint] = obstacle

            results.append(insertionPoint + 1)

        return results