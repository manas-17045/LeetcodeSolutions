# Leetcode 3114: Latest Time You Can Obtain After Replacing Characters
# https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/
# Solved on 15th of September, 2025
class Solution:
    def findLatestTime(self, s: str) -> str:
        """
        Finds the latest possible valid time given a string with '?' characters.
        :param s: A string representing the time, e.g., "0?:3?", "??:??"
        :return: A string representing the latest possible valid time.
        """
        t = list(s)
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'

        if t[0] == '?' and t[1] == '?':
            t[0], t[1] = '1', '1'
        elif t[0] == '?':
            t[0] = '1' if t[1] <= '1' else '0'
        elif t[1] == '?':
            t[1] = '1' if t[0] == '1' else '9'

        return ''.join(t)