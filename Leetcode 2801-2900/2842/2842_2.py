# Leetcode 2842: Count K-Subsequences of a String With Maximum beauty
# https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/
# Solved on 31st of July, 2025
from collections import Counter


class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        """
        Calculates the number of subsequences of a string `s` that have maximum beauty,
        where beauty is defined based on the frequencies of characters.

        :param s: The input string.
        :param k: An integer parameter used in defining beauty.
        :return: The number of subsequences with maximum beauty, modulo 10^9 + 7.
        """
        mod = 10**9 + 7

        # Count and sort frequencies
        freq = sorted(Counter(s).values(), reverse = True)

        # If there aren't enough distinct chars, no valid subsequence
        if k > len(freq):
            return 0
        
        # Find the k-th largest frequency
        f_thresh = freq[k - 1]

        # Count how many chars have exactly that frequency
        total_eq = sum(1 for f in freq if f == f_thresh)
        # And how many of them lie within the top k
        eq_in_top = sum(1 for f in freq[:k] if f == f_thresh)

        # Build product of freq for chars strictly above threshold
        prod = 1
        for f in freq:
            if f > f_thresh:
                prod = prod * f % mod

        # Multiply in the contributions of the threshold-group chars
        prod = prod * pow(f_thresh, eq_in_top, mod) % mod

        # nCr helper function
        def nCr(n: int, r: int) -> int:
            if r < 0 or r > n:
                return 0
            r = min(r, n - r)
            num = den = 1
            for i in range(1, (r + 1)):
                num = num * (n - i + 1) % mod
                den = den * i % mod
            return num * pow(den, mod - 2, mod) % mod
        
        prod = prod * nCr(total_eq, eq_in_top) % mod

        return prod