# Leetcode 3816: Lexicographically Smallest String After Deleting Duplicate Characters
# https://leetcode.com/problems/lexicographically-smallest-string-after-deleting-duplicate-characters/
# Solved on 22nd of January, 2026
from collections import Counter


class Solution:
    def lexSmallestAfterDeletion(self, s: str) -> str:
        """
        Finds the lexicographically smallest string after deleting duplicate characters.

        Args:
            s (str): The input string.

        Returns:
            str: The lexicographically smallest string.
        """
        remaining = Counter(s)
        stackCounts = Counter()
        stack = []

        for char in s:
            remaining[char] -= 1
            while stack and stack[-1] > char:
                top = stack[-1]
                if remaining[top] > 0 or stackCounts[top] > 1:
                    stackCounts[top] -= 1
                    stack.pop()
                else:
                    break

            stack.append(char)
            stackCounts[char] += 1

        while stack:
            top = stack[-1]
            if stackCounts[top] > 1:
                stackCounts[top] -= 1
                stack.pop()
            else:
                break

        return "".join(stack)