# Leetcode 1531: String Compression II
# https://leetcode.com/problems/string-compression-ii/
# Solved on 10th of December, 2025
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded
        version of s has the minimum possible length.

        Args:
            s: The input string.
            k: The maximum number of characters that can be deleted.
        Returns:
            The minimum possible length of the run-length encoded version of s.
        """
        n = len(s)
        memo = {}

        def getMinLength(index, kRemaining):
            if index == n:
                return 0

            state = (index, kRemaining)
            if state in memo:
                return memo[state]

            result = float('inf')

            if kRemaining > 0:
                result = getMinLength(index + 1, kRemaining - 1)

            sameCount = 0
            diffCount = 0
            for i in range(index, n):
                if s[i] == s[index]:
                    sameCount += 1
                    if sameCount == 1:
                        currentLength = 1
                    elif sameCount < 10:
                        currentLength = 2
                    elif sameCount < 100:
                        currentLength = 3
                    else:
                        currentLength = 4

                    if kRemaining >= diffCount:
                        result = min(result, currentLength + getMinLength(i + 1, kRemaining - diffCount))
                else:
                    diffCount += 1
                    if diffCount > kRemaining:
                        break

            memo[state] = result
            return result

        return getMinLength(0, k)