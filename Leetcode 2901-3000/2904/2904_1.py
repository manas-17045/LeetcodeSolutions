# Leetcode 2904: Shortest and Lexicographically Smallest Beautiful String
# https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/
# Solved on 30th of July, 2025
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        """
        Finds the shortest and lexicographically smallest beautiful substring.

        Args:
            s (str): The input binary string.
            k (int): The required number of '1's in the substring.
        Returns:
            str: The shortest and lexicographically smallest beautiful substring, or "" if none exists.
        """
        if s.count('1') < k:
            return ""

        left = 0
        onesCount = 0
        result = ""

        for right in range(len(s)):
            if s[right] == '1':
                onesCount += 1

            while onesCount == k:
                currentSub = s[left: right + 1]

                while s[left] == '0':
                    left += 1
                    currentSub = s[left: right + 1]

                if not result or len(currentSub) < len(result):
                    result = currentSub
                elif len(currentSub) == len(result) and currentSub < result:
                    result = currentSub

                if s[left] == '1':
                    onesCount -= 1
                left += 1

        return result