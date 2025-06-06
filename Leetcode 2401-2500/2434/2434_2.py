# Leetcode 2434: Using a Robot to Print the Lexicographically Smallest String
# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/
# Solved on 6th of June, 2025

class Solution:
    def robotWithString(self, s: str) -> str:
        """
        Given a string s, a robot is located at the beginning of the string.
        The robot can perform two operations:
        1. Take the leftmost character of the string and append it to its paper.
        2. Take the character from the top of its paper and append it to the result string.

        The robot wants to construct the lexicographically smallest possible string.

        This solution uses a stack and a suffix minimum array. The suffix minimum array
        helps determine the smallest character available in the remaining part of the
        original string. The robot greedily appends characters from the stack to the
        result string if the top of the stack is less than or equal to the smallest
        character in the remaining original string.

        Args:
            s: The input string.
        """
        n = len(s)
        # Edge case: If s is empty or length 1, return s immediately
        if n <= 1:
            return s

        # Build suffixMin array, where suffixMin[i] = min(s[i:n - 1])
        suffixMin = [''] * n
        suffixMin[n - 1] = s[n - 1]
        for i in range(n - 2, -1, -1):
            # The smallest character from s[i] and everything to its right
            suffixMin[i] = min(s[i], suffixMin[i + 1])

        stack = []
        answer = []

        # Iterate through s, pushing onto stack, then popping as long as stack[-1] <= next suffixMin.
        for i, ch in enumerate(s):
            stack.append(ch)
            while stack and (i == (n - 1) or stack[-1] <= suffixMin[i + 1]):
                answer.append(stack.pop())

        # Join answer into a single string and return.
        return "".join(answer)