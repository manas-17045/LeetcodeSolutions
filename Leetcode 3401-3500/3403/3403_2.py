# Leetcode 3403: Find the Lexicographically Largest String From the Box I
# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
# Solved on 4th of June, 2025

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        """
        Finds the lexicographically largest string that can be a contiguous substring
        of at least one of the `numFriends` pieces the word is split into.

        Args:
            word: The input string.
            numFriends: The number of friends to split the word among.

        Returns:
            The lexicographically largest string that can be a contiguous substring.
        """
        n = len(word)
        # Special case: If there is exactly 1 friend, you cannot split the word at all,
        # the only valid "chunk" is the entire word.
        if numFriends == 1:
            return word

        # Otherwise, any block that appears among the numFriends contiguous pieces
        # must have length <= n - (numFriends - 1).
        Lmax = n - (numFriends - 1)

        best = ""
        for i in range(n):
            # Take up to Lmax characters starting from i
            candidate = word[i : (i + Lmax)]
            if candidate > best:
                best = candidate

        return best