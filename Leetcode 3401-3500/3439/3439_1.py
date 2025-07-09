# Leetcode 3439: Reschedule Meetings for Maximum Free Time I
# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/
# Solved on 9th of July, 2025
import collections


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: list[int], endTime: list[int]) -> int:
        """
        Calculates the maximum free time achievable by rescheduling at most k meetings.

        Args:
            eventTime (int): The time of the event that needs to be attended.
            k (int): The maximum number of meetings that can be rescheduled.
            startTime (list[int]): A list of start times for each meeting.
            endTime (list[int]): A list of end times for each meeting.

        Returns:
            int: The maximum free time.
        """
        numMeetings = len(startTime)

        meetingDurations = [(endTime[i] - startTime[i]) for i in range(numMeetings)]

        prefixDurations = [0] * (numMeetings + 1)
        for i in range(numMeetings):
            prefixDurations[i + 1] = prefixDurations[i] + meetingDurations[i]

        extendedStarts = startTime + [eventTime]
        extendedEnds = [0] + endTime

        startTerms = [(extendedStarts[i] - prefixDurations[i]) for i in range(numMeetings + 1)]
        endTerms = [(extendedEnds[i] + prefixDurations[i]) for i in range(numMeetings + 1)]

        maxStartTermWindow = [0] * (numMeetings + 1)

        dq = collections.deque()

        for i in range(numMeetings, -1, -1):
            while dq and startTerms[dq[-1]] <= startTerms[i]:
                dq.pop()
            dq.append(i)

            if dq[0] > (i + k):
                dq.popleft()

            maxStartTermWindow[i] = startTerms[dq[0]]

        maxFreeTime = 0
        for i in range(numMeetings + 1):
            currentFreeTime = maxStartTermWindow[i] - endTerms[i]
            if currentFreeTime > maxFreeTime:
                maxFreeTime = currentFreeTime

        return maxFreeTime