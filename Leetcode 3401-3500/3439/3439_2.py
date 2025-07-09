# Leetcode 3439: Reschedule Meetings for Maximum Free Time I
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/
# Solved on 9th of July, 2025
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        """
        Calculates the maximum free time available by removing at most k events.

        Args:
            eventTime (int): The total duration of the event period.
            k (int): The maximum number of events that can be removed.
            startTime (list[int]): A list of start times for each event.
            endTime (list[int]): A list of end times for each event.

        Returns:
            int: The maximum free time achievable.
        """
        n = len(startTime)
        # Compute durations and prefix sums of durations
        dur = [e - s for s, e in zip(startTime, endTime)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + dur[i]

        total_dur = prefix[n]
        if k >= n:
            return eventTime - total_dur

        best = 0
        for ii in range(0, (n - k + 1)):
            j = ii + k
            end_prev = endTime[ii - 1] if ii > 0 else 0
            start_next = startTime[j] if j < n else eventTime
            moved_dur = prefix[j] - prefix[ii]
            free_gap = start_next - end_prev - moved_dur
            if free_gap > best:
                best = free_gap

        return best