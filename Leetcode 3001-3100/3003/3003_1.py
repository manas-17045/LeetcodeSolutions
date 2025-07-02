# Leetcode 3003: Maximize the Number of Partitions After Operations
# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/
# Solved on 2nd of July, 2025
import sys
sys.setrecursionlimit(20000)


class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        """
        Calculates the maximum number of partitions that can be made in a string `s`
        such that each partition has at most `k` distinct characters.
        One operation is allowed to change any character in the string to any other character.

        Args:
            s (str): The input string.
            k (int): The maximum number of distinct characters allowed in a partition.

        Returns:
            int: The maximum number of partitions.
        """
        n = len(s)
        memo = {}

        def solve(index, canChange, currentMask):
            state = (index, canChange, currentMask)
            if index == n:
                return 1

            if state in memo:
                return memo[state]

            # Case 1: Do not change s[index]
            charBit = 1 << (ord(s[index]) - ord('a'))
            newMask = currentMask | charBit

            res = 0
            distinctCount = bin(newMask).count('1')

            if distinctCount > k:
                res = 1 + solve((index + 1), canChange, charBit)
            else:
                res = solve((index + 1), canChange, newMask)

            # Case 2: Change s[index] if allowed
            if canChange:
                for i in range(26):
                    changeCharBit = 1 << i
                    changeMask = currentMask | changeCharBit

                    currentRes = 0
                    # Using popcount again
                    changeDistinctCount = bin(changeMask).count('1')

                    if changeDistinctCount > k:
                        currentRes = 1 + solve((index + 1), False, changeCharBit)
                    else:
                        currentRes = solve((index + 1), False, changeMask)

                    if currentRes > res:
                        res = currentRes

            memo[state] = res
            return res

        if k == 26:
            return 1

        return solve(0, True, 0)