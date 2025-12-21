# Leetcode 3753: Total Waviness of Numbers in Range II
# https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/
# Solved on 21st of December, 2025
from functools import lru_cache


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        """
        Calculates the total waviness of numbers in a given range [num1, num2].
        :param num1: The lower bound of the range (inclusive).
        :param num2: The upper bound of the range (inclusive).
        :return: The total waviness of numbers in the range.
        """
        def count(n):
            s = str(n)
            length = len(s)

            @lru_cache(None)
            def dp(idx, tight, prev, pprev, started):
                if idx == length:
                    return 1, 0

                limit = int(s[idx]) if tight else 9
                resCount = 0
                resWaviness = 0

                for digit in range(limit + 1):
                    newTight = tight and (digit == limit)
                    newStarted = started or (digit > 0)

                    isPeakOrValley = 0
                    if started and pprev != 11:
                        if (prev > pprev and prev > digit) or (prev < pprev and prev < digit):
                            isPeakOrValley = 1

                    nextPrev = prev
                    nextPPrev = pprev

                    if not started:
                        if digit > 0:
                            nextPrev = digit
                            nextPPrev = 11
                        else:
                            nextPrev = 11
                            nextPPrev = 11
                    else:
                        nextPrev = digit
                        nextPPrev = prev

                    c, w = dp(idx + 1, newTight, nextPrev, nextPPrev, newStarted)
                    resCount += c
                    resWaviness += w + (c * isPeakOrValley)

                return resCount, resWaviness

            return dp(0, True, 11, 11, False)[1]

        return count(num2) - count(num1 - 1)