# Leetcode 1189: Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/
# Solved on 22nd of June, 2026
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        Calculates the maximum number of balloons that can be formed from the given text.
        
        :param text: The string of characters to form balloons from.
        :return: The maximum number of balloons that can be formed.
        """
        charCounts = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for textChar in text:
            if textChar in charCounts:
                charCounts[textChar] += 1

        return min(
            charCounts["b"],
            charCounts["a"],
            charCounts["l"] // 2,
            charCounts["o"] // 2,
            charCounts["n"]
        )