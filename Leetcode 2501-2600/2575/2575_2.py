# Leetcode 2575: Find the Divisibility Array of a String
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/
# Solved on 28th of July, 2025
class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:

        """
        Calculates the divisibility array for a given string `word` and integer `m`.

        Args:
            word (str): The input string representing a large number.
            m (int): The divisor.
        Returns:
            list[int]: A list where each element is 1 if the prefix of `word` up to that point is divisible by `m`, and 0 otherwise.
        """
        res: list[int] = []
        curr_mod = 0
        for ch in word:
            # Extend the prefix by one digit and reduce mod m
            curr_mod = (curr_mod * 10 + (ord(ch) - ord('0'))) % m
            # If the prefix mod m is zero, it's divisible
            res.append(1 if curr_mod == 0 else 0)
        return res