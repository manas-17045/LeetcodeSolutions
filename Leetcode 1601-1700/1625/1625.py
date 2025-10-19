# Leetcode 1625: Lexicographically Smallest String After Applying Operations
# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
# Solved on 19th of October, 2025
from collections import deque


class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        """
        Finds the lexicographically smallest string after applying a series of operations.

        Args:
            s (str): The initial string consisting of digits.
            a (int): The value to add to digits at odd indices.
            b (int): The rotation amount.
        Returns:
            str: The lexicographically smallest string achievable.
        """
        queue = deque([s])
        visited = {s}

        smallestString = s

        while queue:
            currentString = queue.popleft()

            if currentString < smallestString:
                smallestString = currentString

            # Operation 1: Add 'a' to odd indices
            addChars = list(currentString)
            for i in range(1, len(addChars), 2):
                newValue = (int(addChars[i]) + a) % 10
                addChars[i] = str(newValue)
            addedString = "".join(addChars)

            if addedString not in visited:
                visited.add(addedString)
                queue.append(addedString)

            # Operation 2: Rotate string by 'b'
            rotatedString = currentString[-b:] + currentString[:-b]

            if rotatedString not in visited:
                visited.add(rotatedString)
                queue.append(rotatedString)

        return smallestString