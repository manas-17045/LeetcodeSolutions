# Leetcode 1585: Check If String Is Transformable With Substring Sort Operations
# https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/
# Solved on 12th of September, 2025
import collections


class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        """
        Checks if string `s` can be transformed into string `t` using substring sort operations.

        Args:
            s (str): The source string.
            t (str): The target string.

        Returns:
            bool: True if `s` can be transformed into `t`, False otherwise.
        """
        if collections.Counter(s) != collections.Counter(t):
            return False

        digitIndices = collections.defaultdict(collections.deque)
        for i, char in enumerate(s):
            digitIndices[char].append(i)

        for targetChar in s:
            sourceIndex = digitIndices[targetChar].popleft()

            targetDigit = int(targetChar)
            for smallerDigit in range(targetDigit):
                smallerChar = str(smallerDigit)
                if digitIndices[smallerChar] and digitIndices[smallerChar][0] < sourceIndex:
                    return False

        return True