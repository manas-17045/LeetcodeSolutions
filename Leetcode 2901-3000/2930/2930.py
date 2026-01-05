# Leetcode 2930: Number of Strings Which Can Be Rearranged to Contain Substring
# https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/
# Solved on 5th of January, 2026
class Solution:
    def stringCount(self, n: int) -> int:
        """
        Calculates the number of strings of length n that can be rearranged to contain the substring "leet".

        Args:
            n: The length of the strings.
        Returns:
            The number of such strings modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7

        totalStrings = pow(26, n, mod)

        sumSingles = (3 * pow(25, n, mod) + n * pow(25, n - 1, mod)) % mod

        sumPairs = (3 * pow(24, n, mod) + 2 * n * pow(24, n - 1, mod)) % mod

        intersectionAll = (pow(23, n, mod) + n * pow(23, n - 1, mod)) % mod

        ans = (totalStrings - sumSingles + sumPairs - intersectionAll) % mod

        return ans