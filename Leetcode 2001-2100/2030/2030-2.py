# Leetcode 2030: Smallest K-Length Subsequence With Occurrences of a Letter
# https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/
# Solved on 30th of August, 2025
class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        """
        Finds the lexicographically smallest subsequence of a given string `s` with specific constraints.

        Args:
            s (str): The input string.
            k (int): The desired length of the subsequence.
            letter (str): A specific character that must appear at least `repetition` times.
            repetition (int): The minimum number of times `letter` must appear in the subsequence.

        Returns:
            str: The lexicographically smallest subsequence.
        """
        n = len(s)
        rem = s.count(letter)
        stack = []
        have = 0

        for i, ch in enumerate(s):
            # Try to pop while it makes lexicographically smaller result AND t's safe to pop
            while stack and stack[-1] > ch and (len(stack) - 1 + (n - i)) >= k:
                if stack[-1] == letter:
                    # If we pop this letter, we must still be able to reach repetition using remaining letters.
                    if have - 1 + rem < repetition:
                        break
                    have -= 1
                    stack.pop()
                else:
                    stack.pop()

            # Decide whether to push current character
            if len(stack) < k:
                if ch == letter:
                    stack.append(ch)
                    have += 1
                else:
                    # Only push a non-letter if after pushing there remains enough slots
                    if k - (len(stack) + 1) >= (repetition - have):
                        stack.append(ch)

            # We've processed current char; if it's special letter, reduce remaining count
            if ch == letter:
                rem -= 1

        return ''.join(stack)