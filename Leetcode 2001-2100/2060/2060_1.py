# Leetcode 2060: Check If an Original String Exists Given Two Encoded Strings
# https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/
# Solved on 14th of August, 2025
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        """
        Checks if two encoded strings can possibly represent the same original string.

        The encoded strings can contain lowercase English letters and digits.
        Digits represent the number of characters they replace.

        Args:
            s1 (str): The first encoded string.
            s2 (str): The second encoded string.
        Returns:
            bool: True if the two encoded strings can represent the same original string, False otherwise.
        """
        lenOne = len(s1)
        lenTwo = len(s2)
        memo = {}

        def solve(i, j, diff):
            if i == lenOne and j == lenTwo:
                return diff == 0

            state = (i, j, diff)
            if state in memo:
                return memo[state]

            # Option 1: s1 parses a number.
            # This can be chosen regardless of the current diff value.
            if i < lenOne and s1[i].isdigit():
                num = 0
                k = i
                while k < lenOne and s1[k].isdigit():
                    num = num * 10 + int(s1[k])
                    k += 1
                    if solve(k, j, diff + num):
                        memo[state] = True
                        return True

            # Option 2: s2 parses a number.
            # This can also be chosen regardless of the diff.
            if j < lenTwo and s2[j].isdigit():
                num = 0
                k = j
                while k < lenTwo and s2[k].isdigit():
                    num = num * 10 + int(s2[k])
                    k += 1
                    if solve(i, k, diff - num):
                        memo[state] = True
                        return True

            # Option 3: Match characters based on the length difference.
            if diff > 0:
                # s1 is ahead, so s2 must provide a literal character to catch up.
                if j < lenTwo and s2[j].isalpha():
                    if solve(i, j + 1, diff - 1):
                        memo[state] = True
                        return True
            elif diff < 0:
                # s2 is ahead, so s1 must provide a literal character.
                if i < lenOne and s1[i].isalpha():
                    if solve(i + 1, j, diff + 1):
                        memo[state] = True
                        return True
            else:  # diff is zero, lengths are balanced.
                # Both must be letters and must match.
                if i < lenOne and j < lenTwo and s1[i].isalpha() and s2[j].isalpha() and s1[i] == s2[j]:
                    if solve(i + 1, j + 1, 0):
                        memo[state] = True
                        return True

            memo[state] = False
            return False

        return solve(0, 0, 0)