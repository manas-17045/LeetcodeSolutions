# Leetcode 2842: Count K-Subsequences of a String With Maximum beauty
# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/
# Solved on 31st of July, 2025
import collections
import math


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        """
        Counts the number of k-subsequences of a string with maximum beauty.

        Args:
            s (str): The input string.
            k (int): The number of distinct characters required in the subsequence.
        Returns:
            int: The number of k-subsequences with maximum beauty, modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        freqCounter = collections.Counter(s)
        
        if len(freqCounter) < k:
            return 0
        
        freqList = sorted(list(freqCounter.values()), reverse=True)

        thresholdFreq = freqList[k - 1]

        ways = 1
        greaterCount = 0
        for freq in freqList:
            if freq > thresholdFreq:
                ways = (ways * freq) % mod
                greaterCount += 1
            else:
                break

        equalCount = freqList.count(thresholdFreq)

        needed = k - greaterCount

        combinations = math.comb(equalCount, needed)

        thresholdWays = pow(thresholdFreq, needed, mod)

        result = (ways * thresholdWays) % mod
        result = (result * combinations) % mod

        return result