# Leetcode 2734: Lexicographically Smallest String After Substring Operation
# https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/
# Solved on 18th of June, 2025

class Solution:
    def smallestString(self, s: str) -> str:
        """
        Given a string s, lexicographically smallest string by performing one operation.
        The operation is to choose a non-empty substring and decrease the alphabetical value of each character in the substring by one.
        'a' becomes 'z'.

        Args:
            s (str): The input string.
        Returns:
            str: The lexicographically smallest string after performing the operation.
        """
        n = len(s)
        # Find first position i where s[i] != 'a'
        i = 0
        while i < n and s[i] == 'a':
            i += 1

        # If entire string is 'a', change only the last one to 'z'
        if i == n:
            # n >= 1 by constraints
            return s[:-1] + 'z'

        # Otherwise, lower the maximal run of non-'a's starting at i
        res = list(s)
        j = i
        while j < n and res[j] != 'a':
            # Shift back by one in the alphabet
            # since res[j] != 'a', ord(res[j]) > ord('a')
            res[j] = chr(ord(res[j]) - 1)
            j += 1

        # Join and return
        return "".join(res)