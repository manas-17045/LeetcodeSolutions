# Leetcode 3986: Number of Elapsed Seconds Between Two Lines
# https://leetcode.com/problems/number-of-elapsed-seconds-between-two-lines/
# Solved on 2nd of August, 2026
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        """
        Calculates the number of elapsed seconds between two given times.

        :param startTime: The starting time in HH:MM:SS format.
        :param endTime: The ending time in HH:MM:SS format.
        :return: The number of elapsed seconds between startTime and endTime.
        """
        startHours, startMinutes, startSeconds = map(int, startTime.split(":"))
        endHours, endMinutes, endSeconds = map(int, endTime.split(":"))

        totalStartSeconds = startHours * 3600 + startMinutes * 60 + startSeconds
        totalEndSeconds = endHours * 3600 + endMinutes * 60 + endSeconds

        return totalEndSeconds - totalStartSeconds