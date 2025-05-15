# Leetcode 2251: Number of Flowers in Full Bloom
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/
# Solved on 15th of May, 2025
from bisect import bisect_right, bisect_left


class Solution:
    def fullBloomFlowers(self, flowers: list[list[int]], people: list[int]) -> list[int]:
        """
        Given a list of flower bloom intervals and a list of people's arrival times,
        determine the number of flowers in full bloom for each person.

        Args:
            flowers: A list of lists, where each inner list represents a flower's
                     bloom interval [start_time, end_time] (inclusive).
            people: A list of integers representing the arrival times of people.

        Returns:
            A list of integers, where each integer represents the number of flowers
            in full bloom at the corresponding person's arrival time.

        Example:
            fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]) == [1,2,2,2]
        """
        # Extract all start times and end times.
        # start_times[i] = start time of flower i
        # end_times[i] = end time of flower i (inclusive, last moment it's in bloom)
        start_times = [flower_interval[0] for flower_interval in flowers]
        end_times = [flower_interval[1] for flower_interval in flowers]

        # Sort these lists to enable binary search
        start_times.sort()
        end_times.sort()

        # Process each person.
        # Pre-allocate the result array for efficiency
        ans = [0] * len(people)

        for i, person_time in enumerate(people):
            # Count flowers that have started blooming by or at person_time (i.e., flower_start_time <= person_time)
            # bisect_right returns an insertion point which is also the count of
            # elements less than or equal to person_time in a sorted list.
            num_started_by_t = bisect_right(start_times, person_time)

            # Count flowers that have ended blooming strictly before person_time
            # (i.e., flower_end_time < person_time)
            # bisect_left returns an insertion point which is also the count of
            # elements strictly less than person_time in a sorted list.
            num_ended_before_t = bisect_left(end_times, person_time)

            # The difference is the count of flowers currently in bloom.
            # A flower [s, e] is in bloom if (s <= person_time) AND (e >= person_time).
            # The term num_started_by_t counts flowers where (s <= person_time).
            # The term num_ended_before_t counts flowers where (e >= person_time).
            # Subtracting removes flowers that started but also ended too early.
            # So, we are left with flowers where (s <= person_time) AND NOT (e < person_time),
            # which is equivalent to (s <= person_time) AND (e >= person_time).
            ans[i] = num_started_by_t - num_ended_before_t

        return ans