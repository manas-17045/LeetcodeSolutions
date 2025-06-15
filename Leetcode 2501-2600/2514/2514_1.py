# Leetcode 2514: Count Anagrams
# https://leetcode.com/problems/count-anagrams
# Solved on 15th of June, 2025
from collections import Counter


class Solution:
    def countAnagrams(self, s: str) -> int:
        """
        Counts the total number of anagrams possible for a given string, considering each word independently.

        Args:
            s: The input string containing words separated by spaces.

        Returns:
            The total number of anagrams modulo 10^9 + 7.
        """
        mod = 10**9 + 7
        words = s.split(' ')

        maxLength = len(s)
        factorials = [1] * (maxLength + 1)
        for i in range(2, (maxLength + 1)):
            factorials[i] = (factorials[i - 1] * i) % mod

        def modularInverse(n):
            return pow(n, (mod - 2), mod)

        numerator = 1
        denominator = 1

        for word in words:
            wordLength = len(word)
            numerator = (numerator * factorials[wordLength]) % mod

            charCounts = Counter(mod)
            for count in charCounts.values():
                denominator = (denominator * factorials[count]) % mod

        result = (numerator * modularInverse(denominator)) % mod

        return result