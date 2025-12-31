# Leetcode 3428: Maximum and Minimum Sums of at Most Size K Subsequences
# https://leetcode.com/problems/maximum-and-minimum-sums-of-at-most-size-k-subsequences/
# Solved on 31st of December, 2025
class Solution:
    def minMaxSums(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of (maximum + minimum) for all subsequences of nums with length at most k.

        Args:
            nums: A list of integers.
            k: The maximum allowed length of a subsequence.
        Returns:
            The total sum of (maximum + minimum) for all valid subsequences, modulo 10^9 + 7.
        """
        mod = 10 ** 9 + 7
        nums.sort()
        n = len(nums)

        fact = [1] * n
        inv = [1] * n
        for i in range(1, n):
            fact[i] = (fact[i - 1] * i) % mod

        inv[n - 1] = pow(fact[n - 1], mod - 2, mod)
        for i in range(n - 2, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % mod

        def getNCr(nVal, rVal):
            if rVal < 0 or rVal > nVal:
                return 0
            numerator = fact[nVal]
            denominator = (inv[rVal] * inv[nVal - rVal]) % mod
            return (numerator * denominator) % mod

        totalSum = 0
        combSum = 1

        for i in range(n):
            currentTerm = (nums[i] + nums[n - 1 - i]) % mod
            contribution = (currentTerm * combSum) % mod
            totalSum = (totalSum + contribution) % mod

            if i < n - 1:
                doubledSum = (combSum * 2) % mod
                subtractTerm = getNCr(i, k - 1)
                combSum = (doubledSum - subtractTerm + mod) % mod

        return totalSum