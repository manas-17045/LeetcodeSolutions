# Leetcode 3114: Latest Time You Can Obtain After Replacing Characters
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/
# Solved on 15th of September, 2025
class Solution:
    def findLatestTime(self, s: str) -> str:
        """
        Replaces '?' characters in a given time string to form the latest possible valid time.

        :param s: A string representing the time, e.g., "0?:3?", "??:??".
        :return: A string representing the latest possible valid time.
        """

        timeList = list(s)

        if timeList[0] == '?':
            if timeList[1] == '?' or timeList[1] <= '1':
                timeList[0] = '1'
            else:
                timeList[0] = '0'

        if timeList[1] == '?':
            if timeList[0] == '1':
                timeList[1] = '1'
            else:
                timeList[1] = '9'

        if timeList[3] == '?':
            timeList[3] = '5'

        if timeList[4] == '?':
            timeList[4] = '9'

        return "".join(timeList)