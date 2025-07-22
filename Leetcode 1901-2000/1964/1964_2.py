# Leetcode 1964: Find the Longest Valid Obstacle Course at Each Position
# https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/
# Solved on 22nd of July, 2025
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: list[int]) -> list[int]:
        """
        Calculates the length of the longest non-decreasing obstacle course ending at each position.

        Args:
            obstacles: A list of integers representing the heights of obstacles.
        Returns:
            A list of integers, where each element at index `i` is the length of the longest non-decreasing
            obstacle course ending at `obstacles[i]`.
        """
        tails: list[int] = []
        ans: list[int] = []

        for h in obstacles:
            # Find rightmost place to extend (allowing equal heights)
            idx = bisect.bisect_right(tails, h)

            if idx == len(tails):
                # New longest non-decr subsequence
                tails.append(h)
            else:
                # Overwrite to keep tail as small as possible
                tails[idx] = h

            ans.append(idx + 1)

        return ans