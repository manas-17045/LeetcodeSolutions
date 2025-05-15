# Leetcode 2251: Number of Flowers in Full Bloom
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/
# Solved on 15th of May, 2025
from bisect import bisect_right, bisect_left


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        """
        Given a list of flower blooming periods (start, end) and a list of people's arrival times,
        determine the number of flowers in full bloom for each person.

        Args:
            flowers: A list of lists, where each inner list represents a flower's blooming period [start, end].
            people: A list of integers representing the arrival times of people.

        Returns: A list of integers, where each integer represents the number of flowers in full bloom for the corresponding person.
        """
        # Extract and sort all start times and end times
        starts = sorted(f for f, _ in flowers)
        ends = sorted(e for _, e in flowers)

        ans = []
        for t in people:
            # Number of flowers that have started by time t
            cnt_start = bisect_right(starts, t)
            # Number of flowers that have already ended before time t
            cnt_end = bisect_left(ends, t)
            # Those in bloom are started but not yet ended
            ans.append(cnt_start - cnt_end)

        return ans