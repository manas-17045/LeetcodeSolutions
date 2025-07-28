# Leetcode 2575: Find the Divisibility Array of a String
# https://leetcode.com/problems/find-the-divisibility-array-of-a-string/
# Solved on 28th of July, 2025
class Solution:
    def divisibilityArray(self, word: str, m: int) -> list[int]:
        """
        Calculates the divisibility array of a given string `word` with respect to an integer `m`.

        Args:
            word (str): The input string representing a large number.
            m (int): The integer to check divisibility against.

        Returns:
            list[int]: A list where each element is 1 if the prefix of `word` up to that point is divisible by `m`, and 0 otherwise.
        """
        divArray = []
        currentRem = 0
        for digitChar in word:
            digit = int(digitChar)
            currentRem = (currentRem * 10 + digit) % m
            if currentRem == 0:
                divArray.append(1)
            else:
                divArray.append(0)

        return divArray