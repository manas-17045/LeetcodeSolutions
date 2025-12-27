# Leetcode 3703: Remove K-Balanced Substrings
# https://leetcode.com/problems/remove-k-balanced-substrings/
# Solved on 27th of December, 2025
class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        """
        Removes k-balanced substrings from the input string s.

        Args:
            s (str): The input string consisting of '(' and ')' characters.
            k (int): The integer value representing the balance factor.
        Returns:
            str: The string after removing all k-balanced substrings.
        """
        stack = []
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append((char, 1))
            else:
                stack.append((char, stack[-1][1] + 1))

            if char == ')' and stack[-1][1] == k:
                if len(stack) >= 2 * k:
                    if stack[-(k + 1)][0] == '(' and stack[-(k + 1)][1] >= k:
                        del stack[-2 * k:]

        return "".join(element[0] for element in stack)