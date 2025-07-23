# Leetcode 1717: Maximum Score From Removing Substrings
# https://leetcode.com/problems/maximum-score-from-removing-substrings/
# Solved on 23rd of July, 2025
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        Calculates the maximum gain by removing "ab" or "ba" substrings.
        :param s: The input string consisting of 'a' and 'b' characters.
        :param x: The score obtained by removing "ab".
        :param y: The score obtained by removing "ba".
        :return: The maximum total score.
        """
        # Decide which substring to remove first
        if x >= y:
            first_pair, first_score = ('a', 'b'), x
            second_pair, second_score = ('b', 'a'), y
        else:
            first_pair, first_score = ('b', 'a'), y
            second_pair, second_score = ('a', 'b'), x

        total = 0
        stack = []
        # First pass: strip out as many first_pair substrings as possible
        for c in s:
            if stack and stack[-1] == first_pair[0] and c == first_pair[1]:
                stack.pop()
                total += first_score
            else:
                stack.append(c)

        # Second pass: strip out the other pair from the leftover characters
        leftover = []
        for c in stack:
            if leftover and leftover[-1] == second_pair[0] and c == second_pair[1]:
                leftover.pop()
                total += second_score
            else:
                leftover.append(c)

        return total