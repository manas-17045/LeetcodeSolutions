# Leetcode 1830: Minimum Number of Operations to Make String Sorted
# https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/
# Solved on 5th of December, 2025
class Solution:
    def makeStringSorted(self, s: str) -> int:
        """
        Calculates the minimum number of operations to make a string sorted.

        Args:
            s: The input string.
        Returns:
            The minimum number of operations modulo 10^9 + 7.
        """
        mod = 1000000007
        n = len(s)

        fact = [1] * (n + 1)
        inv = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = (fact[i - 1] * i) % mod

        inv[n] = pow(fact[n], mod - 2, mod)
        for i in range(n - 1, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % mod

        charCount = [0] * 26
        for char in s:
            charCount[ord(char) - 97] += 1

        denInv = 1
        for count in charCount:
            denInv = (denInv * inv[count]) % mod

        ans = 0
        for i in range(n):
            idx = ord(s[i]) - 97
            smallerCount = sum(charCount[:idx])

            ways = (smallerCount * fact[n - 1 - i]) % mod
            ways = (ways * denInv) % mod
            ans = (ans + ways) % mod

            denInv = (denInv * charCount[idx]) % mod
            charCount[idx] -= 1

        return ans