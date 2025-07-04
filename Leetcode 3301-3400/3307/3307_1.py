# Leetcode 3307: Find the K-th Character in String Game II
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/
# Solved on 4th of July, 2025
class Solution:
    def kthCharacter(self, k: int, operations: list[int]) -> str:
        """
        Finds the k-th character in the final string after a series of operations.

        The problem describes a string game where an initial string "a" undergoes
        a series of operations. Each operation `i` (from 0 to numOps-1) involves:
        1. Appending the current string to itself.
        2. If operations[i] == 1, shifting all characters in the new string by one.

        This solution works backward from the final string to determine the
        original character and its total shift.

        Args:
            k: The 1-indexed position of the character to find.
            operations: A list of integers representing the operations.
        """
        numOps = len(operations)
        totalShift = 0
        currentK = k

        for i in range((numOps - 1), -1, -1):
            operation = operations[i]
            lengthBeforeOp = 2**i

            if currentK > lengthBeforeOp:
                currentK = currentK - lengthBeforeOp
                if operation == 1:
                    totalShift += 1

        finalShift = totalShift % 26
        finalCharCode = ord('a') + finalShift

        return chr(finalCharCode)