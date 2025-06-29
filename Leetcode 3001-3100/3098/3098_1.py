# Leetcode 3098: Find the Sum of Subsequence Powers
# https://leetcode.com/problems/find-the-sum-of-subsequence-powers/
# Solved on 29th of June, 2025
class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        """
        Calculates the sum of powers of all k-length subsequences.

        The power of a subsequence is defined as the minimum absolute difference
        between any two elements in the subsequence.

        Args:
            nums: A list of integers.
            k: The desired length of the subsequences.

        Returns:
            The sum of powers of all k-length subsequences, modulo 1,000,000,007.
        """
        n = len(nums)
        MOD = 1_000_000_007

        nums.sort()

        diffs = set()
        for i in range(n):
            for j in range((i + 1), n):
                diffs.add(nums[j] - nums[i])

        sortedDiffs = sorted(list(diffs))

        totalPowerSum = 0
        prevD = 0

        for d in sortedDiffs:
            dp = [[0] * (k + 1) for _ in range(n)]

            for i in range(n):
                dp[i][1] = 1

            for lenSub in range(2, (k + 1)):
                prefixSum = 0
                pPtr = 0
                for i in range(n):
                    while pPtr < i and nums[i] - nums[pPtr] >= d:
                        prefixSum = (prefixSum + dp[pPtr][lenSub - 1]) % MOD
                        pPtr += 1
                    dp[i][lenSub] = prefixSum

            countD = 0
            for i in range(n):
                countD = (countD + dp[i][k]) % MOD

            term = ((d - prevD) * countD) % MOD
            totalPowerSum = (totalPowerSum + term) % MOD
            prevD = d

        return totalPowerSum