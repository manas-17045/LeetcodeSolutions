# Leetcode 3399: Smallest Substring With Identical Characters II
# https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/
# Solved on 20th of June, 2025

class Solution:
    def minLength(self, s: str, numops: int) -> int:
        """
        Finds the minimum possible length of the string after performing at most `numops` operations.

        The operation involves selecting a substring of length `k` with identical characters
        and replacing it with a single character.

        Args:
            s: The input string consisting of '0's and '1's.
            numops: The maximum number of operations allowed.
        """
        n = len(s)
        if n == 0:
            return 0

        low = 1
        high = n
        ans = n

        while low <= high:
            m = low + (high - low) // 2

            requiredOps = self.getMinOps(s, m)

            if requiredOps <= numops:
                ans = m
                high = m - 1
            else:
                low = m + 1

        return ans

    def getMinOps(self, s: str, k: int) -> int:
        n = len(s)

        if k == 1:
            matchesPattern0101 = 0
            for i in range(n):
                if int(s[i]) == (i % 2):
                    matchesPattern0101 += 1

            flipsForPattern0101 = n - matchesPattern0101
            flipsForPattern1010 = matchesPattern0101

            return min(flipsForPattern0101, flipsForPattern1010)

        opsNeeded = 0
        if n == 0:
            return 0

        currentChar = ''
        currentRunLen = 0

        for i in range(n):
            charVal = s[i]
            if charVal == currentChar:
                currentRunLen += 1
            else:
                if currentRunLen > 0:
                    opsNeeded += currentRunLen // (k + 1)

                currentChar = charVal
                currentRunLen = 1

        if currentRunLen > 0:
            opsNeeded += currentRunLen // (k + 1)

        return opsNeeded